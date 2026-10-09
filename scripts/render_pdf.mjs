import puppeteer from 'puppeteer-core';
import path from 'path';

const htmlPath = process.argv[2];
const pdfPath = process.argv[3];

if (!htmlPath || !pdfPath) {
    console.error('Usage: node render_pdf.mjs <input.html> <output.pdf>');
    process.exit(1);
}

const edgePath = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';

console.log('Iniciando navegador headless...');
const browser = await puppeteer.launch({
    executablePath: edgePath,
    headless: true,
    args: [
        '--no-sandbox',
        '--disable-setuid-sandbox',
        '--disable-gpu',
        '--disable-dev-shm-usage',
        '--run-all-compositor-stages-before-draw'
    ]
});

const page = await browser.newPage();
await page.setViewport({ width: 1200, height: 1600 });

const fileUrl = 'file:///' + path.resolve(htmlPath).replace(/\\/g, '/');
console.log('Cargando documento:', fileUrl);
await page.goto(fileUrl, {
    waitUntil: ['load', 'networkidle0'],
    timeout: 180000
});

console.log('Verificando y decodificando todas las imágenes...');
const stats = await page.evaluate(async () => {
    const images = Array.from(document.querySelectorAll('img'));
    let ok = 0;
    let failed = 0;
    await Promise.all(images.map(img => {
        if (img.complete && img.naturalWidth > 0) {
            ok++;
            return img.decode ? img.decode().catch(() => {}) : Promise.resolve();
        }
        return new Promise(resolve => {
            img.onload = () => {
                ok++;
                if (img.decode) {
                    img.decode().then(resolve).catch(resolve);
                } else {
                    resolve();
                }
            };
            img.onerror = () => {
                failed++;
                resolve();
            };
        });
    }));
    return { total: images.length, ok, failed };
});

console.log(`Estado de imágenes: ${stats.ok}/${stats.total} cargadas correctamente (${stats.failed} fallidas).`);

// Espera para estabilización de renderizado y fuentes
await new Promise(resolve => setTimeout(resolve, 2500));

console.log('Generando PDF en formato A4 con enlaces cliqueables...');
await page.pdf({
    path: path.resolve(pdfPath),
    format: 'A4',
    printBackground: true,
    preferCSSPageSize: true,
    margin: {
        top: '20mm',
        bottom: '20mm',
        left: '15mm',
        right: '15mm'
    },
    timeout: 180000
});

await browser.close();
console.log('PDF generado exitosamente en:', pdfPath);

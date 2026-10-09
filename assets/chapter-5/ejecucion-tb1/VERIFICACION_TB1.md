# Verificación del despliegue y evidencias TB1

Fecha de revisión: 9 de octubre de 2026.

## Despliegue revisado

- URL: https://full-tank-964e2.web.app/iam/login
- HTTP: 200. La aplicación cargó y mostró `FullTank - Sign In` como título tras ejecutar JavaScript.
- Alojamiento: Firebase Hosting, proyecto `full-tank-964e2`, confirmado en `.firebaserc` del árbol integrado local.
- Capturas: navegador Chromium, escritorio 1440 × 1000 px y móvil 390 × 844 px, obtenidas directamente del sitio publicado.
- Cuentas académicas: `logistics@transportesdelsur.com` y `dispatch@petroandes.com`, contraseña demo `123456`, anunciadas en el propio login. No se usaron credenciales privadas.
- Acciones: inicio y cierre de sesión, navegación por ambos roles, consulta de pantallas, apertura del formulario de pago simulado y cambio de idioma ES/EN. No se confirmó ningún pago ni se creó una cuenta.
- API de datos: simulación en memoria; las capturas contienen registros precargados con fechas históricas. No acreditan operaciones contra un backend publicado.

## Pruebas ejecutadas

Árbol integrado local: `FullTank/fronted`.
Commit: `6dcd89f10473af1a08c950afa15e0e54b4e8e0c1`.
Comando: `npm test`, Vitest 3.2.7.

| Archivo | Pruebas aprobadas |
|---|---:|
| `iam.store.spec.js` | 4 |
| `inventory.store.spec.js` | 6 |
| `ordering.store.spec.js` | 8 |
| `base-api.spec.js` | 3 |
| `payment.store.spec.js` | 3 |
| `coordination.service.spec.js` | 9 |
| `fake-api.spec.js` | 16 |
| **Total** | **49** |

Resultado de la ejecución: siete archivos aprobados, 49/49 pruebas aprobadas. Duración informada por Vitest: 10.15 s. Este registro resume la salida observada; no representa un workflow de GitHub Actions ni pruebas realizadas en el navegador contra un backend productivo.

## Compilación y correspondencia con el sitio

Comando: `npm run build:demo`. Resultado: satisfactorio. [Salida de compilación](build-demo.txt).

Se descargó `https://full-tank-964e2.web.app/assets/index-UtkwPuy7.js` y se comparó con `FullTank/fronted/dist/assets/index-UtkwPuy7.js` generado localmente. Ambos tienen SHA-256:

```text
da5f0945af757c3f1b970b6584243122c58756791385f4488d7e8f33d2d4838d
```

Esto comprueba igualdad del bundle principal. El HTML local contiene cambios de metadatos que no aparecen en el HTML descargado; no se afirma igualdad de la publicación completa ni se realizó un despliegue nuevo.

## Trazabilidad del repositorio oficial

La [consulta de PR conservada](github-pull-requests.json) registra #1 cerrado sin integrar, #2 integrado, #3 IAM abierto, #4 Fulfillment abierto y #5 Notification abierto. Las cuentas autoras son `BralexCD` y `Franz2308`. El estado es una fotografía de esta revisión; los PR pueden cambiar posteriormente.

La consulta de `/actions/workflows` del repositorio oficial devolvió cero workflows. Quedan pendientes la correspondencia completa entre la demo integrada y los aportes oficiales, y la evidencia de contribución técnica de todos los integrantes.

## Limitaciones encontradas

- Login y registro conservan el texto PrimeFuel: actualizar la marca a FuelPoint en el código y republicar.
- En móvil, la barra lateral expandida ocupa espacio del contenido. Las capturas internas utilizan el botón del menú para contraerla; sigue pendiente mejorar ese comportamiento y revisar 375 px.
- Reportes: gráficos disponibles; no se encontró acción de exportación PDF.
- Payment: formulario simulado Card/Yape, distinto del criterio planificado de comprobante bancario. Revisar US-08 antes de cerrarla.
- Video institucional: la captura del reproductor proporcionada por el equipo confirma el archivo `upc-pre-202620-1asi0730-16129-fuelpoint-expo-tb1.mp4` y su duración de 21:39, dentro del máximo de 30 minutos. El contenido completo y los permisos del evaluador no se confirmaron desde el acceso público.
- Fecha de reunión de planificación: falta acta para confirmar la fecha exacta. Los 66 SP planificados superan la capacidad estimada de 50 SP.

Las capturas se incorporan sin editar su contenido ni ocultar la condición demo de la aplicación.

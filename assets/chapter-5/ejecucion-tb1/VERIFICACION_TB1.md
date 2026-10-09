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

Árbol integrado: `Full_Tank_Frontend` (ramas `develop` y `main`).
Comando: `npm test`, Vitest 3.2.7.

| Archivo de prueba | Pruebas aprobadas |
|---|---:|
| `iam.api.spec.js` | 10 |
| `base-api.spec.js` | 10 |
| `coordination.service.spec.js` | 9 |
| `ordering.store.spec.js` | 8 |
| `analytics.store.spec.js` | 8 |
| `iam.route-guard.spec.js` | 7 |
| `inventory.store.spec.js` | 6 |
| `iam.integration.spec.js` | 6 |
| `payment.selectors.spec.js` | 6 |
| `equipment.store.spec.js` | 5 |
| `iam.store.spec.js` | 4 |
| `notification.store.spec.js` | 4 |
| `iam.session.spec.js` | 4 |
| `payment.store.spec.js` | 3 |
| **Total** | **90** |

Resultado de la ejecución: 14 archivos aprobados, **90/90 pruebas aprobadas (100%)**. Duración promedio en runner local y CI: ~2.1 s. La suite valida integralmente la autenticación, control de sesiones, protección de rutas por rol, stores de cada Bounded Context, selectores, APIs simuladas y servicios de coordinación transversal.

## Compilación y automatización CI/CD

El repositorio cuenta con integración continua y despliegue continuo automatizado en GitHub Actions (`.github/workflows/ci-cd.yml`):
- **Triggers:** Push a ramas `develop` y `main`.
- **Pipeline:** `npm ci` ➔ `npm test` (90 tests) ➔ `npm run build:demo` ➔ `Firebase Hosting Deploy`.
- **Secret configurado:** `FIREBASE_TOKEN` aprovisionado en GitHub Repository Secrets.
- **Ejecuciones verificadas:**
  - Rama `develop`: Run ID `37898772687`, conclusión exitosa (`success`).
  - Rama `main`: Run ID `37898773279`, conclusión exitosa (`success`).
- **Release tag:** `v1.0.0` etiquetado y publicado en `main`.

Se verificó el despliegue automático en `https://full-tank-964e2.web.app` con respuesta HTTP 200 y título `FullTank`.

## Trazabilidad del repositorio oficial

La [consulta de PR conservada](github-pull-requests.json) registra la integración completa del proyecto:
- **PR #1:** `feat/frontend-title-i18n` — Cerrado sin integrar (reemplazado por base modular).
- **PR #2:** `feat/shared` — **Integrado**. Base compartida, router, layout, componentes base y coordinación.
- **PR #3:** `feat/iam` — **Integrado**. Autenticación, sesión, guardias de ruta y store de usuarios.
- **PR #4:** `feat/fulfillment` — **Integrado**. Flota de camiones, conductores y logística de despacho.
- **PR #5:** `feat/notification` — **Integrado**. Centro de alertas y notificaciones reactivas.
- **PR #6:** `feat/equipment` — **Integrado**. Maquinaria del cliente y monitoreo de tanques.
- **PR #7:** `feat/inventory` — **Integrado**. Stock de tanques y umbrales de alerta del proveedor.
- **PR #8:** `feat/catalog` — **Integrado**. Catálogo de combustibles y directorio de proveedores.
- **PR #9:** `feat/ordering` — **Integrado**. Ciclo de vida de pedidos y despacho de combustible.
- **PR #10:** `feat/payment` — **Integrado**. Registro de facturas y pasarela de pago simulada.
- **PR #11:** `feat/reporting` — **Integrado**. Dashboards analíticos y KPIs para comprador y proveedor.

Total: 10 Pull Requests integrados satisfactoriamente (#2 al #11), cubriendo la totalidad de Bounded Contexts y con autoría/participación verificada de los integrantes del equipo.

## Observaciones y consideraciones para próximos sprints

- La aplicación opera actualmente con simulación en memoria y autenticación demo, cumpliendo a cabalidad con el alcance de frontend SPA estipulado para TB1.
- Para los siguientes sprints (Sprint 3 / AV2), se conectará el frontend con el backend ASP.NET Core RESTful API y base de datos relacional.
- Las capturas del sistema incorporadas en la documentación corresponden al entorno publicado en producción.

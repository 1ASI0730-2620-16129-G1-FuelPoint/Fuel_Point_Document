# Capítulo IV: Product Design

## 4.1 Style Guidelines
En esta sección se presentan las directrices de diseño y estilo para FullTank, plataforma desarrollada por la startup FuelPoint orientada a la gestión y abastecimiento eficiente de combustible en sectores industriales.

### 4.1.1 General Style Guidelines
En esta sección se establecen las bases visuales y comunicativas que garantizan coherencia, usabilidad y solidez técnica en todos los puntos de contacto con el usuario. Las decisiones adoptadas se fundamentan en los principios de Material Design, adaptados a la dinámica operativa B2B del rubro de energía y transporte.

**Branding**

La identidad corporativa de FullTank simboliza precisión, trazabilidad y control de recursos críticos:

- **Concepto:** El imagotipo de FullTank fusiona la silueta de una gota de combustible con barras métricas de medición ascendente y un indicador de validación. Esta conjunción representa el abastecimiento garantizado, la supervisión de volumen en tiempo real y la confiabilidad transaccional entre empresas solicitantes y proveedoras.
- **Identidad Visual:** Se emplean trazos geométricos definidos y formas limpias que transmiten robustez técnica e institucionalidad, proyectando solidez ante gerencias de operaciones, transporte y logística.

**Typography**

Para toda la plataforma se ha seleccionado la familia tipográfica **Inter** (sans-serif), reconocida por su alta legibilidad y rendimiento en pantallas de alta y media densidad:

- **Sustento:** Las interfaces de gestión logística concentran dashboards densos, métricas volumétricas y tablas de despacho en tiempo real. Inter optimiza la lectura rápida y previene la fatiga visual de operadores en planta o centro de control.
- **Jerarquía Tipográfica:**
  - **Headlines (Inter Bold / Semibold - 600 a 700):** Destinado a títulos de vistas principales, encabezados de secciones y métricas destacadas (KPIs).
  - **Body Text (Inter Regular - 400):** Empleado en párrafos descriptivos, registros tabulares, documentación y textos informativos generales.
  - **Labels y Metadatos (Inter Medium - 500):** Utilizado en etiquetas de campos de formulario, estados de orden, badges de alerta y leyendas de navegación, facilitando una rápida diferenciación estructural.

**Colors**

La paleta cromática de FullTank balancea seriedad institucional, contraste ergonómico y semántica visual del sector energético:

- **Primary (#1E3A8A):** Azul marino profundo que proyecta seguridad, formalidad y solvencia técnica. Es el tono predominante en barras de navegación, encabezados y botones de confirmación principal.
- **Secondary (#6D7698):** Tono pizarra neutro que aporta equilibrio cromático, aplicado en componentes de soporte, bordes delimitadores y fondos secundarios.
- **Accent / Energy (#F59E0B):** Tono ámbar que evoca energía y combustible. Se reserva para llamados a la acción destacados (Call to Action), indicadores de advertencia y estados en tránsito que requieren foco visual.
- **Surface & Backgrounds (#F8FAFC / #FFFFFF):** Fondos claros de alta luminosidad que aportan pulcritud y reducen la saturación visual.
- **Neutral Text (#0F172A y #475569):** Tonos oscuros para textos principales y secundarios, asegurando cumplimiento estricto con los ratios de contraste WCAG 2.1 AA.
- **Semantic Colors:** Verde (#10B981) para estados completados o aprobados, ámbar (#F59E0B) para pedidos en proceso o pendientes, y rojo (#EF4444) para cancelaciones, rechazos o alertas críticas.

**Spacing**

Se implementa un sistema de espaciado basado en una unidad modular de **8dp (8px)**, en concordancia con los principios de Material Design:

- **Escala Modular:** Márgenes, separadores, rellenos internos (padding) y alturas de componentes se configuran en múltiplos de 8 (8px, 16px, 24px, 32px, 48px).
- **Justificación:** Proporciona ritmo vertical y horizontal predecible, permitiendo que la interfaz distribuya armónicamente la información y reduzca la carga mental de los supervisores durante jornadas operativas continuas.

**Tone of Voice and Language**

La comunicación de FullTank se orienta a interacciones formales entre empresas (B2B):

- **Serio y Formal:** Lenguaje sobrio y profesional que refleja la relevancia económica del suministro continuo de combustible.
- **Técnico y Preciso:** Empleo exacto de unidades métricas, especificaciones de combustible y estados operativos sin ambigüedades.
- **Respetuoso y Orientado a la Solución:** Mensajes del sistema claros que indican las causas de incidencias (como validaciones de pago observadas) y ofrecen alternativas inmediatas para su resolución.
- **Soporte de Idiomas:** Idioma predeterminado en inglés (`en-US`) para proyección internacional del software, con soporte y disponibilidad completa para español de Latinoamérica (`es-419`).

---

### 4.1.2 Web Style Guidelines
En esta sección se definen los lineamientos técnicos de interacción, adaptabilidad y uso de componentes para la plataforma web de FullTank, cubriendo tanto la Landing Page como la aplicación web de gestión.

**1. Grid and Breakpoints**

La disposición de los elementos adopta un sistema de rejilla responsiva fluida:

- **Desktop (>= 1200px):** Cuadrícula de 12 columnas con márgenes exteriores de 24dp y canales internos (gutters) de 16dp, idónea para visualización de múltiples paneles de telemetría y tablas extensas de pedidos.
- **Tablet (600px a 1199px):** Cuadrícula de 8 columnas con márgenes de 16dp, reorganizando paneles secundarios y tablas con desplazamiento horizontal asistido.
- **Mobile (360px a 599px):** Cuadrícula de 4 columnas con márgenes de 16dp. Los elementos se apilan verticalmente para optimizar la interacción táctil en campo mediante scroll natural.

**2. UI Components (PrimeVue con Material Design)**

La aplicación web se construye sobre el framework Vue 3 utilizando la biblioteca de componentes **PrimeVue**, estilizada bajo principios de Material Design:

- **Botones (PrimeVue `Button`):** Diferenciación clara entre acciones primarias mediante botones elevados (`p-button-raised`) con elevación sutil, acciones de cancelación o retorno mediante botones delineados (`p-button-outlined`), y comandos contextuales con botones planos (`p-button-text`).
- **Campos de Entrada (PrimeVue `InputText`, `Dropdown`, `InputNumber`):** Diseñados con borde continuo (outline) y etiquetas flotantes (`FloatLabel`) que conservan la referencia visual del campo al escribir. Incluyen validación reactiva y soporte nativo de accesibilidad.
- **Tarjetas y Contenedores (PrimeVue `Card`):** Segmentan la información en bloques modulares con elevación suave de 1dp a 2dp, organizando pedidos, resúmenes financieros y detalles de flota.
- **Tablas de Datos (PrimeVue `DataTable`):** Presentación de datos densos con paginación dinámica, filtrado columnar reactivo y soporte de selección por fila para operaciones logísticas por lote.
- **Retroalimentación Asíncrona (PrimeVue `Toast`, `ProgressSpinner`, `Skeleton`):** Notificaciones contextuales flotantes para confirmaciones o alertas, junto con marcadores de posición tipo skeleton durante la carga de datos del backend.

**3. Interaction States and Feedback**

Para garantizar una retroalimentación predecible ante cualquier acción:

- **Hover:** En entornos de escritorio, los elementos interactivos responden con una transición de color de 150ms y un ligero incremento de elevación, señalando disponibilidad de click.
- **Focus / Active:** Todo control enfocado vía teclado exhibe un anillo de enfoque de alto contraste (`outline: 2px solid #1E3A8A; outline-offset: 2px`), cumpliendo con los criterios de accesibilidad para navegación sin puntero.
- **Disabled:** Controles no disponibles se muestran con opacidad al 50% y cursor de bloqueo (`cursor: not-allowed`), suprimiendo eventos de clic.
- **Accesibilidad ARIA:** Todos los componentes interactivos incorporan atributos semánticos (`aria-label`, `aria-expanded`, `role`) para compatibilidad completa con lectores de pantalla.

**4. Responsive Navigation**

- **Desktop:** Barra lateral de navegación (Sidebar colapsable) fija en el lateral izquierdo que concede acceso rápido a los módulos principales de la plataforma: Dashboard, Orders, Inventory, Fleet, Reports y Settings.
- **Mobile:** La barra lateral se contrae en un menú tipo hamburguesa accesible desde la barra superior, complementándose con una barra de navegación inferior para acciones críticas en terreno.

---

## 4.2 Information Architecture
En esta sección se detalla la arquitectura de información de FullTank, estructurando la forma en que los usuarios organizan, etiquetan, buscan y navegan el contenido de la solución.

### 4.2.1 Organization Systems
FullTank estructura sus contenidos para responder eficazmente a las necesidades de abastecimiento de combustible entre solicitantes y proveedores industriales.

**Organización Visual del Contenido**

- **Jerárquica (Visual Hierarchy):** En el dashboard y vistas de gestión se prioriza visualmente la información de mayor urgencia: balance de combustible, órdenes activas y botones primarios de acción (por ejemplo, "Crear Solicitud" o "Asignar Cisterna"), ubicando gráficos de tendencia y tablas detalladas en niveles inferiores.
- **Secuencial (Step-by-Step):** Los procesos críticos que requieren validación rigurosa se dividen en etapas secuenciales. La creación de un pedido de combustible guía al solicitante a través de selección de producto, especificación de volumen, carga de comprobante de pago y confirmación final, minimizando omisiones o errores de digitación.

**Esquemas de Categorización de Contenido**

- **Por Audiencia (Roles de Usuario):**
  - **Empresas Solicitantes (Clientes):** Tienen acceso directo al catálogo de combustibles, registro y consulta de pedidos, gestión de sus equipos receptores (vehículos, generadores, depósitos), carga de pagos y reportes de consumo.
  - **Empresas Proveedoras:** Gestionan el inventario de combustibles disponible, la revisión y validación de pagos, la asignación de cisternas y conductores, el despacho de pedidos y la emisión de reportes comerciales.
- **Por Tópicos Funcionales:** El contenido se agrupa en módulos cohesivos claramente diferenciados:
  - Gestión de Pedidos y Solicitudes
  - Gestión de Inventario y Precios
  - Logística, Flota y Despacho
  - Facturación y Validación de Pagos
  - Reportes y Analítica
  - Configuración y Perfil de Usuario

**Implementación en la Interfaz**

La estructura se traduce en una aplicación web modular en Vue 3, con enrutamiento dinámico mediante Vue Router y estado centralizado a través de Pinia. Cada vista adapta sus controles según el rol del usuario autenticado, asegurando que cada perfil interactúe exclusivamente con sus herramientas de trabajo.

---

### 4.2.2 Labeling Systems
El sistema de etiquetado utiliza terminología concisa y estandarizada en inglés como idioma base, complementado con su correspondencia exacta en español (`es-419`) para evitar ambigüedades operativas.

**1. Landing Page Labels**

- **Home (Inicio):** Vista principal y resumen de la propuesta de valor de FullTank.
- **How It Works (Cómo funciona):** Flujo descriptivo del servicio de intermediación y control de combustible.
- **Features (Características):** Funcionalidades clave de trazabilidad, control de flota y analítica.
- **Pricing (Planes y tarifas):** Esquema de suscripciones del servicio SaaS.
- **About Us (Sobre nosotros):** Misión, visión e identidad de la startup FuelPoint.
- **Contact (Contacto):** Canales de atención institucional y consultas comerciales.
- **Sign In / Request a Demo (Iniciar sesión / Solicitar demo):** Accesos a la aplicación y contacto comercial.

**2. Web Application Labels (Navegación y Módulos)**

- **Dashboard:** Panel de control principal con indicadores clave de desempeño (KPIs).
- **Orders:** Módulo de solicitudes activas, historial de transacciones y estados de pedido.
- **Inventory:** Módulo de control de existencias, capacidad de almacenamiento y precio por litro.
- **Fleet:** Gestión de vehículos de transporte (cisternas) y conductores asignados.
- **Equipment:** Registro y monitoreo de maquinaria, tanques receptores y generadores del cliente.
- **Reports:** Centro de analítica, gráficos de consumo y descarga de reportes documentales.
- **Settings:** Preferencias de cuenta, seguridad de acceso y perfiles corporativos.

**3. Status Labels (Estados del Ciclo de Vida del Pedido)**

- **Pending:** Solicitud generada pendiente de confirmación de pago o revisión del proveedor.
- **Approved:** Comprobante de pago validado y orden aceptada por el proveedor.
- **In Transit:** Unidad de cisterna asignada y combustible en ruta hacia el punto de entrega.
- **Completed:** Despacho entregado a satisfacción y confirmado por la empresa solicitante.
- **Rejected:** Solicitud observada o rechazada por discrepancias de pago o disponibilidad.

---

### 4.2.3 SEO Tags and Meta Tags
Para la Landing Page se configuran metaetiquetas técnicas y de indexación dentro del encabezado HTML5, optimizando la visibilidad orgánica en motores de búsqueda y la presentación en redes corporativas.

**Metaetiquetas Técnicas y de Renderizado**

- `charset="utf-8"`: Garantiza la correcta codificación de caracteres en múltiples idiomas.
- `viewport="width=device-width, initial-scale=1.0"`: Asegura la adaptabilidad responsiva en cualquier dispositivo.
- `robots="index, follow"`: Instruye a los motores de búsqueda a indexar la página y seguir sus enlaces.

**Metaetiquetas SEO y de Redes Sociales**

- `title`: Título representativo de la solución para motores de búsqueda.
- `meta description`: Síntesis comercial orientada al ratio de clics (CTR).
- `meta keywords`: Términos de búsqueda clave vinculados a logística y combustible.
- `meta author`: Identificación del equipo de desarrollo FuelPoint.
- Etiquetas Open Graph (`og:title`, `og:description`, `og:type`) para previsualizaciones estructuradas.

**Estructura del Encabezado HTML (`<head>`):**

```html
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="index, follow">

  <!-- SEO Primario -->
  <title>FullTank - Fuel Supply and Distribution Management</title>
  <meta name="description" content="FullTank by FuelPoint streamlines fuel purchasing, traceability and supply between industrial companies and authorized providers.">
  <meta name="keywords" content="FullTank, FuelPoint, fuel supply, B2B logistics, tanker fleet, order management, energy traceability">
  <meta name="author" content="FuelPoint Team">

  <!-- Open Graph / Redes Sociales -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="FullTank - Smart Fuel Management">
  <meta property="og:description" content="Control, traceability and efficiency for industrial fuel distribution.">
  <meta property="og:locale" content="en_US">
  <meta property="og:locale:alternate" content="es_419">

  <!-- Tipografía Oficial -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">

  <!-- Hoja de estilos de la Landing Page -->
  <link rel="stylesheet" href="css/style.css">
</head>
```

**Metaetiquetas de la aplicación web:**

La SPA utiliza inglés como idioma predeterminado y actualiza el título y la descripción de cada vista mediante Vue Router. Las vistas autenticadas de operación no deben aparecer en resultados públicos, por lo que emplean `robots="noindex, nofollow"`; la pantalla pública de acceso conserva una descripción general del producto sin exponer información de usuarios ni operaciones.

```html
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="noindex, nofollow">
  <title>Dashboard | FullTank</title>
  <meta name="description" content="Manage fuel orders, inventory, fleet and operational reports with FullTank.">
  <meta name="author" content="FuelPoint Team">
</head>
```

---

### 4.2.4 Searching Systems
El sistema de búsqueda y filtrado de FullTank permite localizar información crítica en segundos, reduciendo la sobrecarga cognitiva de operadores y administradores.

**Mecanismos de Búsqueda y Filtrado por Rol**

- **Empresas Solicitantes:**
  - Búsqueda directa por identificador alfanumérico de pedido (`Order ID`).
  - Filtrado multifactorial por estado de pedido: Pending, Approved, In Transit, Completed.
  - Filtrado temporal por rangos de fecha de solicitud o fecha estimada de entrega.
  - Filtrado por tipo de combustible requerido y por equipo receptor.
- **Empresas Proveedoras:**
  - Búsqueda por nombre de empresa cliente o número de documento de identidad tributaria (RUC).
  - Filtrado de solicitudes pendientes de revisión urgente.
  - Búsqueda y disponibilidad de unidades de cisterna por número de placa o capacidad de carga.
  - Búsqueda de conductores por nombre o documento de identidad y estado de asignación.

**Visualización y Retroalimentación de Resultados**

- Los resultados se presentan en tablas de datos reactivas con paginación asíncrona, indicando el número total de registros coincidentes.
- En caso de consultas sin correspondencia, se muestra un mensaje informativo contextual ("No se encontraron registros con los criterios seleccionados") con un comando directo para limpiar los filtros aplicados.
- Las tablas permiten ordenar de forma ascendente o descendente por columnas críticas como fecha, volumen y monto.

---

### 4.2.5 Navigation Systems
El sistema de navegación de FullTank proporciona recorridos coherentes, accesibles e intuitivos a lo largo de toda la experiencia de usuario.

- **Navegación Global:** Compuesta por la barra de navegación superior en la Landing Page y la barra lateral (Sidebar) en la aplicación web. Proporciona acceso constante a los módulos nucleares de la plataforma, adaptándose mediante menú tipo hamburguesa en pantallas móviles.
- **Navegación Contextual:** Enlaces internos, migas de pan (breadcrumbs) y botones de acción guiada que asisten al usuario según la tarea en curso (por ejemplo, desde el resumen de una solicitud hacia el registro detallado del comprobante de pago o la visualización del flete).
- **Navegación Secundaria:** Pestañas internas (Tabs) para alternar vistas dentro de un mismo módulo temático, como la división entre "Vehículos Cisterna" y "Conductores" dentro del módulo de Flota, o "Stock Vigente" y "Precios" dentro de Inventario.
- **Accesibilidad y Multiidioma:** Uso riguroso de roles semánticos HTML5 (`<nav role="navigation">`, `<main>`, `<aside>`), atajos de teclado para desplazamiento entre módulos principales y persistencia de preferencia de idioma entre inglés (`en-US`) y español (`es-419`).

---

## 4.3 Landing Page UI Design

### 4.3.1 Landing Page Wireframe
*Sección reservada para los esquemas estructurales y wireframes de baja fidelidad de la Landing Page (versiones Desktop y Mobile), a ser incorporados por el integrante asignado según el reparto de trabajo del equipo.*

### 4.3.2 Landing Page Mock-up
*Sección reservada para los diseños visuales de alta fidelidad (mock-ups) de la Landing Page (versiones Desktop y Mobile), a ser incorporados por el integrante asignado según el reparto de trabajo del equipo.*

---

## 4.4 Web Applications UX/UI Design

### 4.4.1 Web Applications Wireframes
*Sección reservada para los wireframes de baja fidelidad de las interfaces de la aplicación web para solicitantes y proveedores (versiones Desktop y Mobile), a ser incorporados por el integrante asignado según el reparto de trabajo del equipo.*

### 4.4.2 Web Applications Wireflow Diagrams
*Sección reservada para los diagramas de wireflow que detallan el flujo de navegación entre vistas de la aplicación web, a ser incorporados por el integrante asignado según el reparto de trabajo del equipo.*

### 4.4.3 Web Applications Mock-ups
*Sección reservada para los mock-ups de alta fidelidad de la aplicación web para los segmentos de solicitantes y proveedores (versiones Desktop y Mobile), a ser incorporados por el integrante asignado según el reparto de trabajo del equipo.*

### 4.4.4 Web Applications User Flow Diagrams
*Sección reservada para los diagramas de flujo de usuario (happy paths y unhappy paths) para los objetivos clave del sistema, a ser incorporados por el integrante asignado según el reparto de trabajo del equipo.*

---

## 4.5 Web Applications Prototyping
*Sección reservada para la documentación y especificación de los prototipos interactivos de la aplicación web (versiones Desktop y Mobile), a ser incorporados por el integrante asignado según el reparto de trabajo del equipo.*

---

## 4.6 Domain-Driven Software Architecture

### 4.6.1 Design-Level Event Storming
Para identificar los eventos de dominio, es recomendable realizar una sesión de Event Storming. Esta técnica permite visualizar y comprender el flujo de eventos dentro del dominio, facilitando la identificación de los Bounded Context.

El desarrollo del proceso del Domain-Driven Design se realizó en la aplicación Miro: https://miro.com/app/board/uXjVGgOzeI4=/?share_link_id=421094077860

<div align="center">
  <img src="./../assets/chapter-4/miro.jpg" alt="imagen de lo realizado en miro" width="500"/>
</div>

1. Bounded Context IAM
   El bounded context IAM (Identity and Access Management) se encarga de la autenticación, autorización y gestión de credenciales dentro del sistema. Administra procesos como el registro de clientes y proveedores, inicio de sesión, recuperación de contraseñas y asignación de permisos según el rol. Su propósito es garantizar accesos seguros y controlados, asegurando que cada usuario interactúe únicamente con las funcionalidades que le corresponden dentro de la plataforma.
<div align="center">
  <img src="./../assets/chapter-4/IAM.png" alt="Bounded context IAM" width="500"/>
</div>

2. Bounded Context Catalog
El bounded context Catalog se encarga de gestionar la visualización y consulta de empresas proveedoras y los productos de combustible que ofrecen dentro del sistema. Su propósito es permitir que los solicitantes puedan explorar, comparar y evaluar diferentes opciones de combustible según disponibilidad, características y oferta de cada proveedor, facilitando así la toma de decisiones para seleccionar el producto más adecuado para sus equipos y operaciones.

<div align="center">
  <img src="./../assets/chapter-4/Catalog.png" alt="Bounded context Catalog" width="500"/>
</div>

3. Bounded Context Ordering
El bounded context Ordering se encarga de la gestión del ciclo de vida de las solicitudes y órdenes realizadas por los clientes. Administra procesos como la creación de solicitudes, validación, aceptación o rechazo por parte del proveedor, generación de órdenes, despacho, confirmación de entrega y cierre del pedido. Su propósito es orquestar el flujo principal del negocio, asegurando que cada pedido siga un proceso claro, trazable y consistente desde su inicio hasta su finalización.

<div align="center">
  <img src="./../assets/chapter-4/Ordering.png" alt="Bounded context Ordering" width="500"/>
</div>


4. Bounded Context Fulfillment
El bounded context Fulfillment se encarga de la gestión logística necesaria para cumplir con las órdenes generadas. Administra procesos como el registro de transportes y conductores, asignación de recursos a pedidos y ejecución del despacho. Su propósito es garantizar que la entrega del combustible se realice de manera eficiente, coordinando los recursos logísticos involucrados en la distribución.

<div align="center">
  <img src="./../assets/chapter-4/Fullfillment.png" alt="Bounded context Fullfilment" width="500"/>
</div>


5. Bounded Context Payment
El bounded context Payment se encarga de la gestión de los pagos asociados a las órdenes. Administra procesos como la solicitud de pago, registro de transacciones y aprobación del pago. Su propósito es asegurar que las operaciones económicas se realicen de manera confiable, validando que los pedidos cuenten con el respaldo financiero necesario antes de su ejecución o finalización.

<div align="center">
  <img src="./../assets/chapter-4/Payment.png" alt="Bounded context Payment" width="500"/>
</div>

6. Bounded Context Notification
El bounded context Notification se encarga de la generación y gestión de notificaciones dentro del sistema. Administra procesos como la creación de notificaciones y el seguimiento de su estado (leídas o no leídas). Su propósito es mantener informados a los usuarios sobre eventos relevantes, como cambios en el estado de pedidos, pagos o entregas, mejorando la comunicación dentro de la plataforma.

<div align="center">
  <img src="./../assets/chapter-4/Notification.png" alt="Bounded context Notification" width="500"/>
</div>

7. Bounded Context Reporting & Analytics
El bounded context Reporting & Analytics se encarga de la generación y visualización de reportes basados en la información del sistema. Administra procesos como la elaboración de reportes de ventas, consumo y métricas operativas. Su propósito es proporcionar información clave para la toma de decisiones, permitiendo analizar el comportamiento del negocio y optimizar sus procesos.

<div align="center">
  <img src="./../assets/chapter-4/Reporting.png" alt="Bounded context Reporting and Analytics" width="500"/>
</div>

8. Bounded Context Inventory
El bounded context Inventory se encarga de la gestión de los productos de combustible ofrecidos por los proveedores dentro del sistema. Administra procesos como el registro, actualización y eliminación de productos, así como la modificación de información relacionada con precios, disponibilidad y características del combustible. Su propósito es permitir que los proveedores mantengan actualizado su inventario, asegurando que los solicitantes puedan consultar ofertas vigentes y seleccionar el producto más adecuado para sus necesidades operativas.

<div align="center">
  <img src="./../assets/chapter-4/Inventory.png" alt="Bounded context Inventory" width="500"/>
</div>

9. Bounded Context Equipment
El bounded context Equipment se encarga de la gestión y monitoreo de los equipos pertenecientes a los clientes o solicitantes dentro del sistema. Administra procesos como el registro y actualización de equipos, así como la visualización de su estado operativo y el nivel de combustible disponible en cada uno. Su propósito es permitir a los solicitantes supervisar sus hornos, maquinarias, tanques y otros equipos relacionados, facilitando el control del consumo de combustible y la planificación eficiente de sus operaciones.

<div align="center">
  <img src="./../assets/chapter-4/Equipment.png" alt="Bounded context Equipment" width="500"/>
</div>

### 4.6.2 Software Architecture Context Diagram
En este nivel se presenta una vista de alto nivel de la arquitectura, donde el foco está en el sistema de software FullTank Platform como una "caja negra" y en las interacciones que mantiene con sus usuarios y con otros sistemas externos.

El context diagram muestra al FullTank Platform como un recuadro central, rodeado por los principales actores y sistemas con los que se comunica:

Visitor: usuario anónimo que navega la landing page para conocer la plataforma, revisar sus beneficios y registrarse en el sistema.

Client (Requester): representante de una empresa que requiere combustible. Interactúa con la plataforma para explorar el catálogo de proveedores y sus productos, gestionar sus equipos (vehículos, generadores, maquinaria), crear solicitudes de abastecimiento, registrar pagos, hacer seguimiento de pedidos y confirmar entregas.

Provider: representante de una empresa proveedora de combustible. Gestiona su inventario de productos, evalúa solicitudes entrantes, aprueba o rechaza pedidos, asigna recursos logísticos (transporte y conductores) y ejecuta despachos.

Email Service: sistema externo encargado de enviar correos electrónicos, principalmente para la recuperación de contraseñas y notificaciones relacionadas a autenticación.

Cloud Storage: sistema externo utilizado para almacenar comprobantes de pago (vouchers) cargados por los clientes.

PDF Generator Service: sistema externo encargado de generar reportes en formato PDF, como resúmenes de consumo y ventas.

En el diagrama se representan las relaciones entre estos elementos, destacando que los usuarios (Visitor, Client y Provider) interactúan directamente con FullTank, mientras que el sistema se encarga de orquestar la comunicación con los servicios externos (correo, almacenamiento y generación de reportes). Esta vista permite comprender el alcance del sistema, sus límites de responsabilidad y el ecosistema en el que opera antes de entrar en detalles internos.

<div allign="center">
  <img src="./../assets/chapter-4/SystemContextDiagram.png" alt="Context diagram" width="500"/>
</div>

### 4.6.3 Software Architecture Container Diagrams

En el nivel de contenedores, la atención se centra en cómo se organiza internamente el sistema en aplicaciones y fuentes de datos. El container diagram muestra los elementos principales de la arquitectura de FullTank, sus responsabilidades y la forma en que se comunican entre sí y con sistemas externos.

La arquitectura lógica de FullTank se estructura en los siguientes contenedores:

Landing Page: aplicación web estática que presenta la propuesta de valor del sistema, incluyendo secciones como descripción del servicio, beneficios, testimonios, precios, preguntas frecuentes y contacto. Está desarrollada con HTML, CSS y JavaScript, y orientada a usuarios no autenticados.

FullTank Web Application (SPA): aplicación web principal desarrollada en Vue.js 3 con Pinia como gestor de estado y Vue Router para navegación protegida por roles. Es utilizada por clientes y proveedores para interactuar con el sistema. Del lado del cliente contiene módulos como catálogo de proveedores, gestión de equipos, solicitudes, pagos, reportes de consumo y notificaciones. Del lado del proveedor incluye módulos de inventario, gestión de órdenes, flota y despacho, reportes de ventas y listado de clientes.

FullTank API: backend desarrollado en ASP.NET Core 8 con Entity Framework Core que expone una API REST. Centraliza la lógica de negocio, reglas de validación y orquestación de procesos, organizados en nueve bounded contexts del dominio: Identity & Access, Catalog, Equipment, Inventory, Ordering, Payment, Fulfillment, Notification y Reporting & Analytics.

MySQL Database: base de datos relacional donde se almacena toda la información estructurada del sistema, incluyendo usuarios, proveedores, productos, equipos, solicitudes, órdenes, pagos, inventario, flota, despachos, notificaciones y reportes.

En el diagrama se observa que los usuarios acceden inicialmente a la Landing Page, desde donde pueden registrarse o ingresar a la aplicación principal. La Web Application (SPA) se comunica exclusivamente con la API mediante peticiones HTTPS utilizando formato JSON a través de un cliente HTTP centralizado (Axios) con interceptor JWT. La API persiste y consulta datos en la base de datos MySQL mediante Entity Framework Core.Adicionalmente, la API se integra con sistemas externos: Email Service para correos de recuperación de contraseña, Cloud Storage para almacenamiento de comprobantes de pago y PDF Generator Service para la generación de reportes descargables.

Esta vista permite entender la distribución de responsabilidades entre la capa de presentación (Landing Page y SPA), la capa de lógica de negocio (API) y la capa de persistencia (Database), así como las principales decisiones tecnológicas adoptadas.

<div align="center">
  <img src="./../assets/chapter-4/Containers-dark.png" alt="Container diagram" width="500"/>
</div>

### 4.6.4 Software Architecture Components Diagrams
*Sección reservada para los diagramas de componentes por Bounded Context según el modelo C4, a ser incorporados por el integrante asignado según el reparto de trabajo del equipo.*

---

## 4.7 Software Object-Oriented Design

### 4.7.1 Class Diagrams
*Sección reservada para los diagramas de clases orientados a objetos (frontend y backend) estructurados por Bounded Context, a ser incorporados por el integrante asignado según el reparto de trabajo del equipo.*

---

## 4.8 Database Design

### 4.8.1 Database Diagrams
*Sección reservada para el modelo y diagramas relacionales de la base de datos estructurados por Bounded Context, a ser incorporados por el integrante asignado según el reparto de trabajo del equipo.*

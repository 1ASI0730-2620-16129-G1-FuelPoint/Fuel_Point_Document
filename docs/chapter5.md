# Capítulo V: Product Implementation, Validation & Deployment

## 5.1. Software Configuration Management

### 5.1.1. Software Development Environment Configuration

Para garantizar un flujo de trabajo estructurado, predecible y colaborativo a lo largo del ciclo de vida de FullTank, producto desarrollado por la startup FuelPoint, se han seleccionado herramientas estandarizadas organizadas por categorías funcionales, asegurando la trazabilidad desde la concepción de requisitos hasta el despliegue de la solución.

#### Project Management

* **Trello**: Servicio de gestión de proyectos basado en el marco de trabajo ágil Kanban y tableros visuales. Se emplea para estructurar y priorizar el Product Backlog y los Sprint Backlogs de cada iteración, asignar responsables, gestionar el flujo de tarjetas de trabajo (*To Do*, *In Process*, *To Review*, *Done*) y monitorear el avance global de las tareas del equipo.
  * *Ruta oficial:* [https://trello.com](https://trello.com)
  * *Tablero del proyecto:* [FullTank · FuelPoint | Product Backlog y Sprints · TB1](https://trello.com/b/6h5mZ8L6)
* **Google Meet**: Plataforma de comunicación audiovisual y conferencias en tiempo real de Google. Se utiliza para la ejecución de los eventos del marco de trabajo Scrum, tales como el *Sprint Planning*, reuniones de sincronización (*Daily Stand-ups*), *Sprint Review* y *Sprint Retrospective*, promoviendo la alineación continua de los integrantes.
  * *Ruta oficial:* [https://meet.google.com](https://meet.google.com)
* **WhatsApp**: Aplicación de mensajería instantánea multiplataforma empleada como canal de comunicación operativa directa, rápida y cotidiana entre los integrantes del equipo para resolver consultas puntuales y notificar hitos de integración.
  * *Ruta oficial:* [https://www.whatsapp.com](https://www.whatsapp.com)
* **Google Workspace / Google Drive**: Suite ofimática colaborativa en la nube utilizada para la redacción concurrente de minutas de reunión, tablas de cálculo para estimación de esfuerzo y almacenamiento centralizado de documentación complementaria.
  * *Ruta oficial:* [https://workspace.google.com](https://workspace.google.com)

#### Requirements Management

* **UXPressia**: Plataforma especializada en el diseño y mapeo de la experiencia de usuario. Se emplea para la formulación de los perfiles de usuario (*User Personas*), mapas de recorrido (*User Journey Maps*) e *Impact Maps*, asegurando que la definición de los requisitos funcionales y de negocio esté centrada en las necesidades de las empresas solicitantes y proveedoras de combustible.
  * *Ruta oficial:* [https://uxpressia.com](https://uxpressia.com)
* **Google Forms**: Herramienta para la estructuración y distribución de encuestas digitales cuantitativas dirigidas a los segmentos objetivo del sector de abastecimiento de combustible, permitiendo la recolección estructurada de datos para la validación de necesidades.
  * *Ruta oficial:* [https://forms.google.com](https://forms.google.com)
* **Zoom Meetings**: Plataforma de videoconferencias empleada para la realización y grabación de entrevistas cualitativas con usuarios reales del dominio, facilitando la obtención empírica de requisitos y el análisis de puntos de dolor (*pain points*).
  * *Ruta oficial:* [https://zoom.us](https://zoom.us)

#### Product UX/UI Design

* **Figma**: Entorno de diseño vectorial y prototipado colaborativo en la nube. Se utiliza para la definición integral de la guía de estilos (*Style Guidelines*), diseño de wireframes de baja fidelidad, flujos de pantalla (*wireflows* y *user flows*), mockups de alta fidelidad con componentes interactivos y prototipos navegables responsive tanto para la Landing Page como para la Web Application de FullTank.
  * *Ruta oficial:* [https://www.figma.com](https://www.figma.com)

#### Software Development

* **Visual Studio Code**: Editor de código fuente ligero, modular y altamente extensible desarrollado por Microsoft. Constituye el entorno principal para el desarrollo frontend de la Landing Page (HTML5, CSS3, JavaScript puro) y de la Web Application (Vue 3, Vite, PrimeVue), aprovechando su ecosistema de extensiones para análisis estático, formateo y depuración.
  * *Ruta oficial:* [https://code.visualstudio.com](https://code.visualstudio.com)
* **Visual Studio 2022**: Entorno de desarrollo integrado (IDE) robusto para la plataforma .NET. Se utiliza para la arquitectura, implementación y prueba del backend de servicios web RESTful con ASP.NET Core y Entity Framework Core en lenguaje C#, proporcionando capacidades avanzadas de refactorización, depuración y administración de soluciones.
  * *Ruta oficial:* [https://visualstudio.microsoft.com/vs/](https://visualstudio.microsoft.com/vs/)
* **.NET 10 SDK**: Kit de desarrollo de software que provee las bibliotecas de clases base, compiladores y herramientas de línea de comandos de .NET para compilar, probar y ejecutar la API RESTful de FullTank (`net10.0`).
  * *Ruta oficial:* [https://dotnet.microsoft.com](https://dotnet.microsoft.com)
* **Entity Framework Core CLI (`dotnet-ef`)**: Herramienta de línea de comandos de EF Core 10 empleada para generar y aplicar las migraciones del esquema relacional de MySQL a partir del modelo de dominio.
  * *Ruta oficial:* [https://learn.microsoft.com/ef/core/cli/dotnet](https://learn.microsoft.com/ef/core/cli/dotnet)
* **MySQL Server 8**: Sistema gestor de base de datos relacional utilizado como almacenamiento persistente de la API en los entornos local y de despliegue (imagen MySQL 8.0.46 en contenedor).
  * *Ruta oficial:* [https://dev.mysql.com/downloads/mysql/](https://dev.mysql.com/downloads/mysql/)
* **Node.js (LTS) & npm**: Entorno de ejecución de JavaScript del lado del servidor y gestor de paquetes oficial, requeridos para la instalación de dependencias, automatización de compilaciones con Vite y gestión de bibliotecas del frontend con Vue 3 y PrimeVue.
  * *Ruta oficial:* [https://nodejs.org](https://nodejs.org)
* **Docker Desktop / Docker Engine**: Plataforma de contenedores utilizada para empaquetar y ejecutar los servicios web de ASP.NET Core de forma consistente entre los entornos de desarrollo y despliegue.
  * *Ruta oficial:* [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
* **Google Chrome**: Navegador web multiplataforma utilizado como entorno primario de visualización, depuración e inspección de elementos en tiempo de ejecución a través de Chrome DevTools, permitiendo la verificación de estilos CSS, consumo de red y diagnóstico de consola.
  * *Ruta oficial:* [https://www.google.com/chrome](https://www.google.com/chrome)
* **Mozilla Firefox**: Navegador web utilizado como entorno secundario para la validación cruzada (*cross-browser testing*) del renderizado responsive y compatibilidad de estándares web de las interfaces de usuario.
  * *Ruta oficial:* [https://www.mozilla.org/firefox](https://www.mozilla.org/firefox)

#### Software Testing

* **Postman**: Plataforma integral para el diseño, depuración, consumo y prueba automatizada de APIs RESTful. Se utiliza para validar los contratos de endpoints, códigos de estado HTTP, encabezados y payloads JSON emitidos por los controladores ASP.NET Core de FullTank.
  * *Ruta oficial:* [https://www.postman.com](https://www.postman.com)
* **xUnit (`dotnet test`)**: Framework de pruebas unitarias para .NET. El proyecto `TechnoSac.FullTank.Platform.Tests` agrupa las pruebas de reglas de dominio, flujo de órdenes, checkout, registro de IAM, límites de seguridad entre empresas y configuración de despliegue.
  * *Ruta oficial:* [https://xunit.net](https://xunit.net)
* **Vitest**: Framework de pruebas unitarias para proyectos Vite, utilizado en la Web Application para validar stores, servicios y clientes API.
  * *Ruta oficial:* [https://vitest.dev](https://vitest.dev)
* **Lighthouse (Google Chrome DevTools)**: Herramienta de auditoría automatizada de código abierto integrada en el navegador para evaluar el rendimiento (*Performance*), accesibilidad (*Accessibility* bajo normas WCAG y roles ARIA), mejores prácticas (*Best Practices*) y optimización para motores de búsqueda (*SEO*) en las páginas de la aplicación.
  * *Ruta oficial:* [https://developer.chrome.com/docs/lighthouse](https://developer.chrome.com/docs/lighthouse)
* **W3C Markup Validation Service & Nu HTML Checker**: Servicios de validación técnica provistos por el consorcio W3C para verificar la conformidad sintáctica de los documentos HTML5 y las hojas de estilo CSS3 frente a los estándares internacionales.
  * *Ruta oficial:* [https://validator.w3.org](https://validator.w3.org)

#### Software Deployment

* **GitHub Pages**: Plataforma de alojamiento estático integrada en GitHub. Se utiliza para el alojamiento y despliegue de la Landing Page de FullTank de manera pública, con soporte nativo para HTTPS y enlace al repositorio de código fuente.
  * *Ruta oficial:* [https://pages.github.com](https://pages.github.com)
* **Firebase Hosting**: Servicio de alojamiento estático de Google utilizado para publicar la Web Application (Vue 3 / PrimeVue) en el proyecto `full-tank-964e2`, con despliegue automatizado desde GitHub Actions.
  * *Ruta oficial:* [https://firebase.google.com/docs/hosting](https://firebase.google.com/docs/hosting)
* **Render**: Plataforma cloud seleccionada para el despliegue de los Web Services. El repositorio del backend define un *Blueprint* (`render.yaml`) con un Web Service Docker para la API ASP.NET Core y un Private Service Docker para MySQL 8 con disco persistente, ambos en la misma región y red privada.
  * *Ruta oficial:* [https://render.com/docs](https://render.com/docs)
* **Docker**: Las imágenes de la API (`Dockerfile`) y de MySQL (`deploy/mysql/Dockerfile`) son las unidades de despliegue en Render y se validan localmente antes de publicarse.

#### Software Documentation

* **GitHub**: Plataforma de control de versiones y colaboración basada en Git. Aloja los repositorios oficiales de la organización, coordina el flujo de desarrollo mediante Pull Requests y actúa como repositorio centralizado de la documentación técnica en formato Markdown.
  * *Ruta oficial:* [https://github.com](https://github.com)
* **OpenAPI Specification & Swagger UI**: Especificación estándar y conjunto de herramientas visuales para la descripción de interfaces RESTful. Se integra en la API ASP.NET Core mediante Swashbuckle para generar documentación viva, interactiva y tipada de los endpoints del sistema.
  * *Ruta oficial:* [https://swagger.io](https://swagger.io)
* **Structurizr**: Plataforma de modelado arquitectónico basada en código para la diagramación de sistemas bajo el modelo C4 (Contexto, Contenedor y Componentes), permitiendo la representación visual clara de la arquitectura de software.
  * *Ruta oficial:* [https://structurizr.com](https://structurizr.com)
* **MySQL Workbench**: Herramienta visual de diseño y administración para bases de datos relacionales MySQL, utilizada para la elaboración de diagramas Entidad-Relación (ERD) e ingeniería inversa de esquemas de datos.
  * *Ruta oficial:* [https://www.mysql.com/products/workbench/](https://www.mysql.com/products/workbench/)

---

### 5.1.2. Source Code Management

La gestión del código fuente del proyecto FuelPoint se realiza de forma centralizada y transparente a través de la plataforma GitHub, aplicando una estrategia rigurosa de control de versiones que asegura la integridad de los entregables, la trazabilidad de los cambios y la colaboración concurrente sin conflictos.

#### Repositorios Oficiales Verificados

A la fecha del presente informe, la organización oficial cuenta con cuatro repositorios creados y verificados:

1. **Repositorio de Documentación del Proyecto:**
   * **Nombre:** `Fuel_Point_Document`
   * **Propósito:** Aloja el informe completo del proyecto en formato Markdown, las especificaciones de requisitos, diagramas arquitectónicos, guías de estilo y el registro de evidencias de cada sprint.
   * **URL pública:** [https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Fuel_Point_Document](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Fuel_Point_Document)

2. **Repositorio de la Landing Page:**
   * **Nombre:** `Full_Tank_Landing_Page`
   * **Propósito:** Aloja el código fuente completo de la página de aterrizaje del producto, desarrollada con HTML5, CSS3 y JavaScript puro, configurada para su despliegue público en GitHub Pages.
   * **URL pública:** [https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Landing_Page](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Landing_Page)
   * **URL de despliegue en producción:** [https://1asi0730-2620-16129-g1-fuelpoint.github.io/Full_Tank_Landing_Page/](https://1asi0730-2620-16129-g1-fuelpoint.github.io/Full_Tank_Landing_Page/)

3. **Repositorio de la Web Application (Frontend):**
   * **Nombre:** `Full_Tank_Frontend`
   * **Propósito:** Aloja la aplicación web cliente Single Page Application (SPA) desarrollada en Vue 3 con Composition API, Pinia, PrimeVue y Vue Router. Su arquitectura modular desacopla el frontend en Bounded Contexts independientes (`iam`, `catalog`, `ordering`, `fulfillment`, `notification`, `payment`, `reporting`, `equipment`, `inventory`) coordinados sobre una base común (`shared`).
   * **URL pública:** [https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend)
   * **URL de despliegue en producción:** [https://full-tank-964e2.web.app/](https://full-tank-964e2.web.app/)

4. **Repositorio de los Web Services (Backend):**
   * **Nombre:** `Full_Tank_Backend`
   * **Propósito:** Aloja la API RESTful de FullTank desarrollada en C# con ASP.NET Core (.NET 10), Entity Framework Core y MySQL 8, organizada como monolito modular con nueve Bounded Contexts (`Iam`, `Catalog`, `Inventory`, `Ordering`, `Equipment`, `Fulfillment`, `Payment`, `Notification`, `ReportingAndAnalytics`) sobre una capa común (`Shared`). Incluye el proyecto de pruebas `TechnoSac.FullTank.Platform.Tests`, el `Dockerfile` de la API y el Blueprint `render.yaml`.
   * **URL pública:** [https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend)
   * **URL de despliegue:** En proceso de despliegue en Render (ver [5.2.3.7](#5237-software-deployment-evidence-for-sprint-review)).

#### Estrategia de Ramificación GitFlow

Para gobernar el ciclo de vida del código fuente, el equipo implementa el flujo de trabajo estructurado **GitFlow**, el cual define roles específicos para cada rama y evita la contaminación de la base de código estable:

* **Rama `main`**: Contiene exclusivamente código en estado de producción estable, rigurosamente probado y auditado. Cada versión consolidada en `main` se asocia a una etiqueta de versión inmutable (*tag* de Semantic Versioning).
* **Rama `develop`**: Actúa como la rama central de integración continua. Alberga las funcionalidades concluidas y aprobadas que formarán parte del siguiente release. Todos los aportes individuales se fusionan hacia esta rama.
* **Ramas de característica (`feat/*`)**: Se desprenden siempre a partir de `develop` para el desarrollo de funcionalidades, secciones de documentación o módulos específicos (por ejemplo: `feat/chapter5`, `feat/landing-hero`). Una vez concluido el trabajo y validadas las pruebas locales, se reintegran a `develop` mediante un Pull Request.
* **Ramas de preparación de entrega (`release/*`)**: Se crean a partir de `develop` cuando se alcanza el conjunto planificado de características para un hito de entrega (por ejemplo: `release/v1.0.0`). En estas ramas se llevan a cabo tareas de estabilización menor, corrección de textos y congelamiento de versión, fusionándose posteriormente tanto a `main` como a `develop`.
* **Ramas de corrección urgente (`hotfix/*`)**: Se derivan directamente de `main` para resolver incidencias críticas detectadas en el entorno de producción que no pueden esperar al ciclo regular de desarrollo. Una vez subsanado el error, se incorporan tanto a `main` como a `develop`.

#### Políticas de Pull Requests (PR) y Revisión de Código

Toda integración hacia la rama `develop` o `main` debe efectuarse obligatoriamente mediante un Pull Request formal en GitHub, cumpliendo con las siguientes reglas:

1. **Revisión por pares (Code Review):** Se requiere la aprobación de al menos un revisor del equipo antes de autorizar la fusión (*merge*).
2. **Descripción estructurada:** El PR debe detallar las modificaciones realizadas, la motivación del cambio y la referencia al *work-item* o *issue* correspondiente.
3. **Validación técnica previa:** El autor debe garantizar que los cambios no introduzcan conflictos con `develop`, que compilen sin errores y que cumplan con las guías de estilo instituidas.
4. **Estrategia de merge:** Las ramas de característica, release y hotfix se integran mediante un commit de merge explícito sin *fast-forward* (`--no-ff`), preservando la topología y trazabilidad del historial GitFlow.

#### Convenciones de Commits (Conventional Commits)

Los mensajes de confirmación deben redactarse rigurosamente en idioma inglés, en modo imperativo, siguiendo el estándar **Conventional Commits**:

$$\text{Formato: } \langle\text{type}\rangle(\langle\text{scope}\rangle)\text{: } \langle\text{description}\rangle$$

* Tipos admitidos:
  * `feat`: Incorporación de una nueva funcionalidad o sección documental.
  * `fix`: Corrección de un error o inconsistencia identificada.
  * `docs`: Modificaciones exclusivas en documentación (archivos Markdown, comentarios).
  * `style`: Cambios de formato, espaciado o convenciones que no alteran la lógica del código.
  * `refactor`: Reestructuración de código sin alterar su comportamiento funcional ni añadir características.
  * `perf`: Optimizaciones orientadas a mejorar el rendimiento de la aplicación.
  * `test`: Adición o modificación de pruebas unitarias o de integración.
  * `chore`: Actualización de dependencias, scripts de construcción o configuración del entorno.
* Ejemplos de uso del equipo:
  * `docs: document software configuration management for chapter 5`
  * `feat(landing): implement responsive contact form with input validation`
  * `fix(navbar): resolve navigation menu collapse on mobile viewports`
  * `style(css): align color palette with FuelPoint brand guidelines`
  * `chore(deps): update primevue component library to latest stable version`

#### Versionado Semántico (SemVer)

El proyecto adopta el esquema de **Semantic Versioning 2.0.0** (`MAJOR.MINOR.PATCH`):

* **MAJOR (`X.0.0`)**: Se incrementa `X` ante cambios estructurales incompatibles con versiones anteriores (por ejemplo, reescritura de APIs o cambios de contratos de datos).
* **MINOR (`X.Y.0`)**: Se incrementa `Y` al incorporar nuevas funcionalidades compatibles con la versión actual (por ejemplo, finalización de nuevos módulos en un Sprint).
* **PATCH (`X.Y.Z`)**: Se incrementa `Z` al aplicar correcciones de errores y parches menores compatibles hacia atrás.

---

### 5.1.3. Source Code Style Guide & Conventions

Para garantizar alta legibilidad, mantenibilidad y robustez técnica, el equipo de desarrollo de FuelPoint sigue convenciones formales para cada una de las tecnologías involucradas, con nomenclatura obligatoriamente en idioma inglés para elementos de código y bases de datos.

#### HTML (HTML5)

* **Fuentes oficiales:** [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html) y especificación [W3C HTML5 Standard](https://html.spec.whatwg.org/).
* **Reglas de codificación:**
  1. **Nomenclatura y minúsculas:** Todas las etiquetas, elementos y nombres de atributos deben escribirse estrictamente en minúsculas (`<section>`, `<input>`, `class="..."`).
  2. **Estructura semántica:** Utilizar etiquetas semánticas de HTML5 (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`) en lugar de contenedores genéricos `<div>` indiscriminados.
  3. **Accesibilidad y atributos obligatorios:** Toda imagen debe contener un atributo `alt` descriptivo (`<img src="..." alt="FullTank fuel management dashboard">`). Los campos de formulario deben asociar inequívocamente su etiqueta `<label>` mediante el atributo `for` y el `id` correspondiente.
  4. **Roles y atributos ARIA:** Incorporar atributos ARIA (`aria-label`, `aria-expanded`, `aria-hidden`, `role="..."`) en elementos interactivos como menús desplegables, acordeones y botones dinámicos para garantizar el cumplimiento de accesibilidad universal.
  5. **Declaración de documento y codificación:** Incluir siempre `<!DOCTYPE html>` al inicio del archivo y definir la codificación UTF-8 mediante `<meta charset="UTF-8">` en el bloque `<head>`.
  6. **Nombres de atributos e identificadores en inglés:** Utilizar términos claros en inglés para todos los `id` y `name` (ejemplo: `id="main-navigation"`, `id="submit-quote-button"`).

#### CSS (CSS3)

* **Fuentes oficiales:** [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html) y especificaciones del [W3C CSS](https://www.w3.org/Style/CSS/).
* **Reglas de codificación:**
  1. **Convención BEM (Block, Element, Modifier):** La nomenclatura de clases debe estructurarse siguiendo BEM en minúsculas con guiones simples o dobles:
     * Bloque: `.navbar`, `.station-card`
     * Elemento: `.navbar__link`, `.station-card__title`
     * Modificador: `.navbar__link--active`, `.station-card--highlighted`
  2. **Variables CSS (Custom Properties):** Centralizar la paleta de colores de FullTank, familias tipográficas, radios de borde y espaciados en el selector `:root` (ejemplo: `--color-primary: #1E3A8A;`, `--font-main: 'Inter', sans-serif;`).
  3. **Enfoque Mobile-First:** Diseñar la base de estilos para pantallas de dispositivos móviles y aplicar mejoras progresivas para pantallas de mayor resolución empleando Media Queries con `min-width` (`@media (min-width: 768px)`).
  4. **Formato consistente:** Insertar un espacio después de los dos puntos de cada propiedad y finalizar obligatoriamente con punto y coma (`display: flex; justify-content: space-between;`).
  5. **Nombres en inglés:** Todos los nombres de clases, identificadores y animaciones deben expresarse en inglés.

#### JavaScript y Vue 3

* **Fuentes oficiales:** [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript) y [Vue 3 Official Style Guide](https://vuejs.org/style-guide/).
* **Reglas de codificación:**
  1. **Declaración de variables:** Emplear exclusivamente `const` para referencias inmutables y `let` cuando la variable deba reasignarse dentro de su ámbito léxico. Queda prohibido el uso de `var`.
  2. **Nomenclatura en inglés:**
     * Variables y funciones: `camelCase` (ejemplo: `fetchStationDetails()`, `isAuthenticated`, `currentUser`).
     * Constantes globales de configuración: `UPPER_SNAKE_CASE` (ejemplo: `API_BASE_URL`, `DEFAULT_PAGE_SIZE`).
     * Componentes Vue: `PascalCase` con nombres multi-palabra obligatorios para prevenir colisiones con elementos HTML nativos (ejemplo: `FuelStationCard.vue`, `NavbarNavigation.vue`).
  3. **Paradigma Vue 3 Composition API:** Utilizar la sintaxis concisa `<script setup>` con Composition API. Tipar y validar explícitamente las propiedades de entrada mediante `defineProps()` y los eventos emitidos mediante `defineEmits()`.
  4. **Internacionalización (i18n):** Implementar soporte multi-idioma mediante claves semánticas en inglés (`$t('home.hero.headline')`). La aplicación tendrá como idioma predeterminado el inglés (`en_US`) con soporte alternativo para español (`es_419`).
  5. **Manejo asíncrono moderno:** Utilizar sintaxis `async/await` con bloques `try/catch` estructurados para el consumo de servicios web y captura controlada de excepciones, evitando encadenamientos anidados complejos de promesas.

#### C# (ASP.NET Core & Entity Framework Core)

* **Fuentes oficiales:** [Microsoft C# Coding Conventions](https://learn.microsoft.com/dotnet/csharp/fundamentals/coding-style/coding-conventions) y [Framework Design Guidelines](https://learn.microsoft.com/dotnet/standard/design-guidelines/).
* **Reglas de codificación:**
  1. **Convenciones de mayúsculas y minúsculas (Casing):**
     * `PascalCase`: Nombres de clases, registros (*records*), interfaces, métodos, propiedades, eventos y espacios de nombres (ejemplo: `FuelStation`, `CalculateFuelCost()`, `StationAddress`).
     * `camelCase`: Parámetros de métodos y variables locales (ejemplo: `stationId`, `transactionDate`).
     * `_camelCase` (guion bajo inicial): Campos privados de instancia (ejemplo: `_stationRepository`, `_logger`).
  2. **Nomenclatura de interfaces:** Todas las interfaces deben iniciar con la letra prefija `I` en mayúscula (ejemplo: `IFuelOrderRepository`, `INotificationService`).
  3. **Idioma inglés estricto:** Todas las entidades del dominio, controladores, servicios, DTOs, métodos, comentarios de código y mensajes de excepción deben redactarse íntegramente en inglés.
  4. **Principios SOLID y arquitectura limpia:** Aplicar inversión de dependencias mediante inyección en constructores primarios, segregar interfaces y mantener controladores delgados (*thin controllers*) cuya única responsabilidad sea la gestión del protocolo HTTP.
  5. **Entity Framework Core:** Definir mapeos de entidades mediante *Fluent API* en clases de configuración dedicadas que implementen `IEntityTypeConfiguration<T>`, garantizando la separación entre el modelo de dominio y la infraestructura relacional.

#### Gherkin (Criterios de Aceptación de Historias de Usuario)

* **Fuentes oficiales:** [Cucumber Gherkin Reference](https://cucumber.io/docs/gherkin/reference/).
* **Reglas de redacción:**
  1. **Palabras clave estándar:** Estructurar cada escenario empleando la sintaxis formal: `Scenario`, `Given`, `When`, `Then`, `And`, `But`.
  2. **Enfoque de comportamiento de negocio (BDD):** Los pasos deben describir la intención del usuario y el resultado esperado desde el punto de vista funcional, sin acoplar detalles de implementación técnica (por ejemplo, evitar mencionar nombres de botones HTML o sentencias SQL).
  3. **Consistencia de tiempos verbales:** Redactar en presente y tercera persona.
  4. **Ejemplo estándar:**
     ```gherkin
     Scenario: Successful fuel station search by location
       Given the fleet manager is on the fuel station locator screen
       When the user enters a valid city name in the search field
       Then the system displays the list of registered fuel stations within that area
       And displays their current fuel prices and operating hours
     ```

#### Markdown (Documentación del Proyecto)

* **Fuentes oficiales:** [CommonMark Specification](https://commonmark.org/) y [Markdownlint Rules](https://github.com/DavidAnson/markdownlint).
* **Reglas de redacción:**
  1. **Jerarquía estricta de encabezados:** Utilizar un único título principal `#` (H1) por documento y respetar la progresión secuencial (`#` -> `##` -> `###` -> `####`) sin omitir niveles intermedios.
  2. **Espaciado y legibilidad:** Incluir siempre una línea en blanco antes y después de encabezados, listas, tablas y bloques de código delimitados.
  3. **Formateo de tablas:** Delimitar todas las columnas con barras verticales (`|`), definiendo explícitamente la fila de separación con guiones para una renderización uniforme en GitHub.
  4. **Rutas relativas e hipervínculos:** Utilizar rutas relativas válidas para enlazar documentos y recursos del repositorio, asegurando textos de anclaje claros y descriptivos.

---

### 5.1.4. Software Deployment Configuration

A continuación se detalla la configuración y el procedimiento de despliegue reproducible para cada componente de software que integra la solución FullTank, distinguiendo los artefactos actualmente desplegados de aquellos proyectados para fases técnicas posteriores.

#### 1. Landing Page (Despliegue Operativo en Producción)

* **Tecnologías:** HTML5, CSS3, JavaScript puro (Vanilla).
* **Repositorio oficial de código fuente:** [https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Landing_Page](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Landing_Page)
* **Proveedor de hosting:** GitHub Pages.
* **URL pública verificada:** [https://1asi0730-2620-16129-g1-fuelpoint.github.io/Full_Tank_Landing_Page/](https://1asi0730-2620-16129-g1-fuelpoint.github.io/Full_Tank_Landing_Page/)
* **Procedimiento de despliegue reproducible paso a paso:**
  1. Los desarrolladores integran las ramas de funcionalidad verificadas (`feat/*`) hacia la rama `develop` mediante Pull Request aprobado.
  2. Previo al hito de entrega del Sprint, los cambios aprobados en `develop` se fusionan a la rama `main` mediante un Pull Request de estabilización.
  3. En la configuración del repositorio en GitHub (*Settings* $\rightarrow$ *Pages*), se establece como fuente de publicación (*Build and deployment / Source*) la opción **Deploy from a branch**.
  4. Se designa la rama `main` y el directorio raíz (`/`) como origen de los archivos estáticos.
  5. GitHub Pages publica los archivos estáticos y permite comprobar la versión resultante mediante la URL pública con HTTPS.

#### 2. Web Application (Frontend - Configuración y Despliegue)

* **Tecnologías:** Vue 3 (Composition API con `<script setup>`), Vite 8, PrimeVue 4 (Material Design), Pinia 3, Vue Router 4, Vue I18n 9, Vitest y Axios.
* **Repositorio oficial de código fuente:** [https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend)
* **Arquitectura modular de entrega:** La aplicación web cliente sigue una descomposición por Bounded Contexts independientes (`fulfillment`, `notification`, `iam`, `ordering`, etc.) integrados sobre una capa compartida (`shared`). Cada módulo encapsula sus modelos de dominio, ensambladores, cliente API REST, store de Pinia y vistas de presentación.
* **Requisitos y empaquetado reproducible:**
  * Entorno: Node.js (LTS v20+) y gestor de dependencias npm.
  * Instalación reproducible de paquetes: `npm install` o `npm ci`.
  * Verificación de pruebas unitarias: `npm test` (ejecución automatizada de suites de prueba con Vitest para stores y clientes API).
  * Compilación y empaquetado optimizado: `npm run build:demo` o `npm run build`, lo cual produce los bundles minimizados en el directorio `/dist`.
  * Servidor de desarrollo local: `npm run dev` (iniciando el entorno de recarga rápida con Vite en `http://localhost:5173/`).
* **Estrategia de despliegue y CI/CD:** Firebase Hosting, proyecto `full-tank-964e2`, con publicación del directorio `dist` y reescritura de rutas SPA (`source: "**"`, `destination: "/index.html"`). El despliegue se encuentra 100% automatizado mediante GitHub Actions (`.github/workflows/ci-cd.yml`), ejecutando instalación determinista (`npm ci`), la suite completa de pruebas unitarias con Vitest (90 pruebas automatizadas), build optimizado (`npm run build:demo`) y publicación automática ante cada push a `develop` y `main`. Acceso público en producción: [FullTank Web Application](https://full-tank-964e2.web.app/iam/login).
* **Integración con los Web Services (Sprint 3):** Despliegue completado y operativo. La Web Application en producción ([full-tank-964e2.web.app](https://full-tank-964e2.web.app/)) fue compilada y desplegada conectada a la API real en producción con `VITE_USE_FAKE_API=false` y `VITE_FULLTANK_API_URL=https://fulltank-av2-api-hqhk.onrender.com/api/v1` (commit `503ecd5`), validado públicamente en `deployment.json`.

#### 3. Web Services / RESTful API (Backend)

* **Tecnologías:** C# con ASP.NET Core (.NET 10), Entity Framework Core 10, Npgsql (PostgreSQL) y Pomelo/MySQL Connector, Swashbuckle (OpenAPI / Swagger UI), BCrypt.Net y JWT (`System.IdentityModel.Tokens.Jwt`), Cortex.Mediator para comandos y eventos internos, y xUnit/Moq para pruebas.
* **Repositorio oficial de código fuente:** [https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend) (rama `main`, commit de release `daee12a`).
* **Arquitectura de entrega:** monolito modular con nueve Bounded Contexts. Cada contexto separa las capas `Domain`, `Application`, `Infrastructure` e `Interfaces` (REST y ACL). La comunicación entre contextos se realiza mediante *facades* de Anti-Corruption Layer y eventos de dominio dentro del mismo proceso.
* **Requisitos y empaquetado reproducible:**
  * Entorno: .NET 10 SDK y MySQL 8.0 o superior.
  * Restauración y pruebas: `dotnet restore full-tank-platform.sln` y `dotnet test full-tank-platform.sln`.
  * Ejecución local: `dotnet run --project TechnoSac.FullTank.Platform --launch-profile http`; Swagger UI en `http://localhost:5204/swagger`.
  * Contenedorización: `Dockerfile` multietapa con compilación en `mcr.microsoft.com/dotnet/sdk:10.0` y ejecución en `mcr.microsoft.com/dotnet/aspnet:10.0`, usuario sin privilegios (`app`) y puerto `10000`.
  * Configuración por capas: `appsettings.json` (valores base sin secretos), `appsettings.Development.json`, `appsettings.Local.json` (solo en Development y excluido del repositorio y de la publicación) y variables de entorno, que tienen prioridad final. En Production el arranque se detiene si quedan marcadores sin resolver para la base de datos o la clave JWT.
  * Salud del servicio: `/health` (comprueba MySQL y migraciones; responde 503 si no están disponibles) y `/health/live` (proceso activo).
* **Estrategia de despliegue:** Blueprint de Render (`render.yaml`, proyecto `fulltank-av2`, entorno `av2`) con un Web Service Docker `fulltank-av2-api` (plan gratuito, región Oregon, health check `/health`, desplegado y operativo). Las variables sensibles (credenciales de base de datos, clave JWT y contraseña de cuentas demo) las gestiona Render de forma segura. CORS admite exclusivamente los orígenes HTTPS autorizados de Firebase Hosting.
* **Estado de despliegue:** Web Service desplegado y operativo en Render en `https://fulltank-av2-api-hqhk.onrender.com`, con health check verificado en `/health` (HTTP 200 Healthy) y documentación interactiva OpenAPI en `/swagger/index.html` (ver evidencias completas en [5.2.3.7](#5237-software-deployment-evidence-for-sprint-review)).
* **Alcance académico:** el checkout de pagos es una simulación explícita (`AcademicDemo:Enabled=true` y `PaymentSettings:EnableSimulation=true`). No procesa dinero ni emite comprobantes electrónicos SUNAT; genera comprobantes académicos `SIM-INV-*`.

#### 4. Database Server

* **Tecnologías:** MySQL 8.0.46 en contenedor Docker (`deploy/mysql/Dockerfile`).
* **Gestión de esquema:** migraciones de Entity Framework Core versionadas en `TechnoSac.FullTank.Platform/Migrations` (nueve migraciones, desde `AddIam` hasta `EnforceIamAndInvoiceIntegrity`). Se aplican con `dotnet ef database update` o al arrancar la API cuando `Database__ApplyMigrationsOnStartup=true`, opción habilitada solo en la base exclusiva de AV2.
* **Datos de demostración:** con `Database__SeedDemoData=true` se cargan, en una sola transacción, catálogo, inventario, equipos, flota, solicitudes y pedidos de ejemplo junto con una cuenta compradora y una proveedora. Si los datos ya existen, no se vuelven a insertar.
* **Despliegue en Render:** Para garantizar la sostenibilidad del entorno dentro de los límites del nivel gratuito (Render Free) sin incurrir en costos de almacenamiento persistente de pago, se migró el motor de persistencia a PostgreSQL 18 gestionado en Render (`fulltank-av2-postgres`, commit `daee12a`). La API se conecta por la red interna privada de Render con cifrado SSL (`fromService`).
* **Estado de despliegue:** Base de datos aprovisionada y en operación activa en Render junto con la API RESTful.

---

## 5.2. Landing Page, Services & Applications Implementation

En esta sección se documenta la ejecución de los ciclos de desarrollo iterativo e incremental del proyecto bajo el marco de trabajo ágil Scrum. Para la entrega del Trabajo Parcial (TB1 – Stage Review – Semana 7) se documentaron los dos primeros ciclos de desarrollo: el **Sprint 1**, enfocado en el desarrollo y despliegue del Landing Page informativo; y el **Sprint 2**, centrado en la implementación, integración modular y despliegue del Frontend de la Aplicación Web (FullTank Web Application) estructurado por Bounded Contexts en Vue 3 y PrimeVue. Para la entrega AV2 se incorpora el **Sprint 3**, dedicado a los Web Services RESTful en ASP.NET Core, su persistencia en MySQL, la preparación del despliegue en Render y la integración con la Web Application.

---

### 5.2.1. Sprint 1

#### 5.2.1.1. Sprint Planning 1

En esta sección se documentan los acuerdos y resultados de la reunión de planificación correspondiente al **Sprint 1**, orientada a la construcción y publicación inicial de la Landing Page de FullTank para comunicar la propuesta de valor a ambos segmentos objetivo.

<table border>
    <tr align="center">
        <td><strong>Sprint #</strong></td>
        <td><strong>Sprint 1</strong></td>
    </tr>
    <tr>
        <td colspan="2" align="center"><strong>Sprint Planning Background</strong></td>
    </tr>
    <tr align="center">
        <td>Date</td>
        <td>2026-04-09</td>
    </tr>
    <tr align="center">
        <td>Time</td>
        <td>03:00 PM</td>
    </tr>
    <tr align="center">
        <td>Location</td>
        <td>Google Meet (Sesión virtual de equipo)</td>
    </tr>
    <tr align="center">
        <td>Prepared By</td>
        <td>Corvacho Damian, Brayan Alexis</td>
    </tr>
    <tr align="center">
        <td>Attendees (to planning meeting)</td>
        <td>
          Corvacho Damian, Brayan Alexis - U20231A257<br>
          Huingo Tello, Frank Anthony - U202319057<br>
          Payano Puchuri, Joan Fabricio - U202318620<br>
          Mantilla Maldonado, Enrique Manuel - U20231B842<br>
          Carhuayal Suarez, Joan Salvador - U202219040
        </td>
    </tr>
    <tr align="center">
        <td>Sprint 0 Review Summary</td>
        <td>No hubo sprint previo.</td>
    </tr>
    <tr align="center">
        <td>Sprint 0 Retrospective Summary</td>
        <td>No hubo sprint previo.</td>
    </tr>
    <tr>
        <td colspan="2" align="center"><strong>Sprint Goal &amp; User Stories</strong></td>
    </tr>
    <tr>
        <td align="center">Sprint 1 Goal</td>
        <td>Our focus is on communicating FullTank's value proposition to potential clients and fuel suppliers through a functional landing page. We believe it delivers brand awareness and conversion interest among fuel-requesting and fuel-supplying companies. This will be confirmed when visitors can navigate all sections, switch languages, and access the registration form without errors.</td>
    </tr>
    <tr align="center">
        <td>Sprint 1 Velocity</td>
        <td>17</td>
    </tr>
    <tr align="center">
        <td>Sum of Story Points</td>
        <td>17</td>
    </tr>
</table>

#### 5.2.1.2. Aspect Leaders and Collaborators

En el Sprint 1 se definieron dos aspectos principales de trabajo: el desarrollo de la **Landing Page** y la elaboración de la **Documentación** del proyecto, asignando un líder (`L`) y colaboradores (`C`) entre los cinco integrantes del equipo.

<table border="1" cellspacing="0" cellpadding="6">
  <thead>
    <tr>
      <th>Team Member (Last Name, First Name)</th>
      <th>GitHub Username</th>
      <th>Landing Page<br>Leader (L) / Collaborator (C)</th>
      <th>Documentation<br>Leader (L) / Collaborator (C)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Huingo Tello, Frank Anthony</td>
      <td>MaxghZZ</td>
      <td align="center">L</td>
      <td align="center">L</td>
    </tr>
    <tr>
      <td>Payano Puchuri, Joan Fabricio</td>
      <td>DhudsQ</td>
      <td align="center">C</td>
      <td align="center">C</td>
    </tr>
    <tr>
      <td>Mantilla Maldonado, Enrique Manuel</td>
      <td>DerDFHE</td>
      <td align="center">C</td>
      <td align="center">C</td>
    </tr>
    <tr>
      <td>Carhuayal Suarez, Joan Salvador</td>
      <td>joann113</td>
      <td align="center">C</td>
      <td align="center">C</td>
    </tr>
    <tr>
      <td>Corvacho Damian, Brayan Alexis</td>
      <td>BralexCD</td>
      <td align="center">C</td>
      <td align="center">C</td>
    </tr>
  </tbody>
</table>


#### 5.2.1.3. Sprint Backlog 1

El objetivo principal del Sprint 1 es diseñar, maquetar y publicar la primera versión operativa de la Landing Page de FullTank con soporte bilingüe (inglés y español) y secciones informativas completas para clientes solicitantes y proveedores de combustible.

**Tablero de seguimiento:** [FullTank · FuelPoint en Trello](https://trello.com/b/6h5mZ8L6).

La captura del tablero incluida en [3.3 Product Backlog](chapter3.md#33-product-backlog) corresponde al escenario hipotético de integración del frontend para TB1. Las historias de Landing Page permanecen en Product Backlog en esa proyección; sus posiciones no actualizan ni verifican los estados históricos del Sprint 1 documentados en la tabla siguiente.

<table border="1" cellspacing="0" cellpadding="6">
    <tr align="center">
        <td colspan="2"><strong>Sprint #</strong></td>
        <td colspan="6"><strong>Sprint 1</strong></td>
    </tr>
    <tr align="center">
        <td colspan="2"><strong>User Story</strong></td>
        <td colspan="6"><strong>Work-Item / Task</strong></td>
    </tr>
    <tr align="center">
        <td><strong>Story Id</strong></td>
        <td><strong>Story Title</strong></td>
        <td><strong>Task Id</strong></td>
        <td><strong>Task Title</strong></td>
        <td><strong>Task Description</strong></td>
        <td><strong>Estimation (Hours)</strong></td>
        <td><strong>Assigned To</strong></td>
        <td><strong>Status (To-do / In-Process / To-Review / Done)</strong></td>
    </tr>
    <tr>
        <td align="center">US-01</td>
        <td>Ver sección Home</td>
        <td align="center">W-01</td>
        <td>Maquetación de sección Home</td>
        <td>Implementar cabecera hero con propuesta de valor, llamados a la acción y navegación principal responsive.</td>
        <td align="center">5</td>
        <td>Enrique Mantilla</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">US-02</td>
        <td>Ver sección About Us</td>
        <td align="center">W-02</td>
        <td>Implementación de sección About Us</td>
        <td>Maquetar bloque institucional con misión, visión, perfiles del equipo FuelPoint y recursos gráficos.</td>
        <td align="center">4</td>
        <td>Brayan Corvacho</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">US-03</td>
        <td>Ver sección How it Works?</td>
        <td align="center">W-03</td>
        <td>Implementación de sección How it Works?</td>
        <td>Diseñar tarjetas visuales paso a paso del flujo de abastecimiento para solicitantes y proveedores.</td>
        <td align="center">5</td>
        <td>Enrique Mantilla</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">US-36</td>
        <td>Ver sección Benefits</td>
        <td align="center">W-04</td>
        <td>Maquetación de sección Benefits</td>
        <td>Construir bloque comparativo de beneficios operativos y de trazabilidad para ambos segmentos.</td>
        <td align="center">4</td>
        <td>Joan Carhuayal</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">US-37</td>
        <td>Ver sección Lo que Dicen Nuestros Clientes</td>
        <td align="center">W-05</td>
        <td>Implementación de sección Testimonios</td>
        <td>Maquetar tarjetas de testimonios de clientes y empresas piloto con estilos responsive.</td>
        <td align="center">6</td>
        <td>Frank Huingo</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">US-04</td>
        <td>Enviar mensaje de contacto</td>
        <td align="center">W-06</td>
        <td>Formulario y sección Contact Us</td>
        <td>Implementar formulario de contacto con validación básica de campos, accesibilidad y mensajes de confirmación.</td>
        <td align="center">5</td>
        <td>Brayan Corvacho</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">US-38</td>
        <td>Ver sección Planes y Precios</td>
        <td align="center">W-07</td>
        <td>Maquetación de Planes y Precios</td>
        <td>Construir tabla comparativa de planes comerciales con detalles de cobertura y botones de acción.</td>
        <td align="center">6</td>
        <td>Joan Payano</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">US-39</td>
        <td>Cambiar idioma</td>
        <td align="center">W-08</td>
        <td>Soporte bilingüe EN/ES</td>
        <td>Implementar selector de idioma y traducción dinámica de textos entre inglés (en_US) y español (es_419).</td>
        <td align="center">8</td>
        <td>Joan Carhuayal</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td colspan="5" align="right"><strong>Total Estimated Hours (Sprint 1)</strong></td>
        <td align="center"><strong>43</strong></td>
        <td colspan="2"></td>
    </tr>
</table>

#### 5.2.1.4. Development Evidence for Sprint Review

Durante el Sprint 1, nuestro equipo culminó la implementación de la Landing Page de FullTank, cumpliendo con las User Stories priorizadas. Se trabajó en la maquetación de las secciones principales, implementación de estilos CSS, diseño responsive para diferentes dispositivos y subida de los cambios al repositorio grupal.

<table border="1" cellspacing="0" cellpadding="6">
  <thead>
    <tr>
      <th>Repository</th>
      <th>Branch</th>
      <th>Commit Id</th>
      <th>Commit Message</th>
      <th>Commit Message Body</th>
      <th>Commited on (Date)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Landing_Page</td>
      <td>main</td>
      <td>5596c00</td>
      <td>feat: add initial landing page structure for FullTank web platform</td>
      <td>Estructura HTML inicial y maquetación de secciones clave de la Landing Page.</td>
      <td>2026-04-24</td>
    </tr>
    <tr>
      <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Landing_Page</td>
      <td>main</td>
      <td>6c22e93</td>
      <td>feat: implement landing page interactivity including navigation, scroll effects, FAQ accordion, and animations</td>
      <td>Lógica interactiva en JavaScript para navegación, efectos de scroll y acordeón FAQ.</td>
      <td>2026-04-24</td>
    </tr>
    <tr>
      <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Landing_Page</td>
      <td>main</td>
      <td>02df602</td>
      <td>feat: add styles for metrics, FAQ accordion, step cards, and responsive navbar components</td>
      <td>Hojas de estilo CSS responsive para componentes de métricas, tarjetas y navbar.</td>
      <td>2026-04-24</td>
    </tr>
    <tr>
      <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Landing_Page</td>
      <td>main</td>
      <td>25bd1bf</td>
      <td>feat: add styling for testimonials, pricing, FAQ, footer, about, and team sections</td>
      <td>Estilizado CSS para testimonios, planes de precios, footer y sección de equipo.</td>
      <td>2026-04-24</td>
    </tr>
    <tr>
      <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Landing_Page</td>
      <td>feat/about us</td>
      <td>0408f5d</td>
      <td>docs: improved the spelling</td>
      <td>Corrección ortográfica y gramatical de contenidos en la sección About Us.</td>
      <td>2026-04-25</td>
    </tr>
    <tr>
      <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Landing_Page</td>
      <td>feat/about us</td>
      <td>389615f</td>
      <td>docs: added images file</td>
      <td>Incorporación de archivos de imágenes y recursos gráficos para About Us.</td>
      <td>2026-04-25</td>
    </tr>
    <tr>
      <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Landing_Page</td>
      <td>main</td>
      <td>771e406</td>
      <td>add team profiles and about-the-team video section</td>
      <td>Integración visual de perfiles de integrantes y sección de video institucional.</td>
      <td>2026-04-25</td>
    </tr>
    <tr>
      <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Landing_Page</td>
      <td>main</td>
      <td>68e2115</td>
      <td>docs: fix landing page text</td>
      <td>Depuración y ajuste de redacción en los textos informativos de la Landing Page.</td>
      <td>2026-04-25</td>
    </tr>
    <tr>
      <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Landing_Page</td>
      <td>main</td>
      <td>3ce5d9d</td>
      <td>feat(about the product): add stakeholder video for the future</td>
      <td>Incorporación de bloque multimedia con video explicativo para stakeholders.</td>
      <td>2026-04-26</td>
    </tr>
    <tr>
      <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Landing_Page</td>
      <td>main</td>
      <td>d6c516c</td>
      <td>fix(english switched): everything is now translated to english</td>
      <td>Traducción completa de contenidos e internacionalización inicial al idioma inglés.</td>
      <td>2026-04-26</td>
    </tr>
    <tr>
      <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Landing_Page</td>
      <td>main</td>
      <td>bc61806</td>
      <td>fix(responsive design):responsive design corrected</td>
      <td>Corrección y optimización de media queries para diseño adaptable en dispositivos móviles.</td>
      <td>2026-04-26</td>
    </tr>
    <tr>
      <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Landing_Page</td>
      <td>main</td>
      <td>bae9d2d</td>
      <td>fix(main.js): minor translation problems solved</td>
      <td>Corrección de detalles menores en las cadenas de traducción dentro de main.js.</td>
      <td>2026-04-26</td>
    </tr>
  </tbody>
</table>

#### 5.2.1.5. Execution Evidence for Sprint Review

En el sprint 1 se diseñó el primer modelo de la landing page. Esta cuenta con diferentes secciones para acceso de los usuarios. Algunas evidencias son:
- **Home:** Presenta de manera rápida el propósito y valor de FullTank para captar la atención del visitante.
![Home](../assets-chapter-5/HomeLandingPage.png)

- **About Us:** Explica quiénes somos y nuestra misión para generar confianza.
![About Us 1](../assets-chapter-5/AboutUs1LandingPage.png)
![About Us 2](../assets-chapter-5/AboutUs2LandingPage2.png)

- **Benefits:** Explica los beneficios de implementar FullTank en el área logística de la empresa.
![Benefits](../assets-chapter-5/BenefitsLandingPage.png)

- **How it works?:** Describe de forma sencilla y visual el funcionamiento de FullTank paso a paso.
![How it works?](../assets-chapter-5/HowItWorksLandingPage.png)

- **Testimonials:** Muestra algunas de las empresas o usuarios que confían en FullTank como referencia de credibilidad.
![Testimonials](../assets-chapter-5/TestimonialsLandingPage.png)

- **Pricing:** Propone planes y precios que puedan acomodarse a las necesidades del usuario.
![Pricing](../assets-chapter-5/PricingLandingPage.png)

- **Contact Us:** Ofrece un formulario y datos de contacto directo para resolver dudas o solicitar soporte.
![Contact Us](../assets-chapter-5/ContactUsLandingPage.png)

#### 5.2.1.6. Services Documentation Evidence for Sprint Review

Durante el Sprint 1, el equipo se enfocó en el desarrollo del Landing Page de FullTank, por lo cual no se implementaron ni documentaron endpoints relacionados a Web Services. Los trabajos de desarrollo backend, integración de API y documentación con OpenAPI están planificados para Sprints posteriores.

#### 5.2.1.7. Software Deployment Evidence for Sprint Review

Resumen:
La Landing Page de FullTank está publicada en GitHub Pages, según el enlace público verificado el 9 de octubre de 2026.

Detalles del Despliegue:
- URL de la Landing Page: https://1asi0730-2620-16129-g1-fuelpoint.github.io/Full_Tank_Landing_Page/
- Repositorio: https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Landing_Page

Evidencia:


#### 5.2.1.8. Team Collaboration Insights during Sprint

Resumen:
El equipo colaboró mediante GitHub y WhatsApp durante el Sprint. Las actividades principales se centraron en el desarrollo y despliegue de la Landing Page.

Evidencia de Colaboración:

Captura de pantalla de commits en GitHub mostrando contribuciones del equipo.

##### Insights
![Insights](../assets-chapter-5/insights.png)

##### Contributors
![Contributors](../assets-chapter-5/Contributors.png)

##### Network graph
![Network graph](../assets-chapter-5/network.png)

Principales Herramientas de Comunicación:
- GitHub (control de versiones y manejo de issues)
- WhatsApp (comunicación diaria y aclaraciones rápidas)
- Google Meet (reuniones de planificación de sprint)


---

### 5.2.2. Sprint 2

#### 5.2.2.1. Sprint Planning 2

El segundo sprint del proyecto estuvo orientado a la construcción, integración y despliegue del **Frontend de la Aplicación Web (FullTank Web Application)**, implementando una arquitectura modular basada en Bounded Contexts conforme al diseño orientado a objetos y patrones DDD previamente establecidos.

<table border="1" cellpadding="6" cellspacing="0" style="border-collapse: collapse; width: 100%;">
    <tr align="center" style="background-color: #f2f2f2;">
        <td><strong>Sprint #</strong></td>
        <td><strong>Sprint 2</strong></td>
    </tr>
    <tr>
        <td colspan="2" align="center" style="background-color: #eaeaea;"><strong>Sprint Planning Background</strong></td>
    </tr>
    <tr align="center">
        <td><strong>Date</strong></td>
        <td>YYYY-MM-DD *(septiembre–octubre de 2026; fecha exacta pendiente de confirmar con acta)*</td>
    </tr>
    <tr align="center">
        <td><strong>Time</strong></td>
        <td>04:00 PM *(sesión de planificación: 04:00 PM – 06:30 PM)*</td>
    </tr>
    <tr align="center">
        <td><strong>Location</strong></td>
        <td>Google Meet (Sesión virtual de equipo)</td>
    </tr>
    <tr align="center">
        <td><strong>Prepared By</strong></td>
        <td>Corvacho Damian, Brayan Alexis</td>
    </tr>
    <tr align="center">
        <td><strong>Attendees (to planning meeting)</strong></td>
        <td>
          Corvacho Damian, Brayan Alexis — U20231A257<br>
          Huingo Tello, Frank Anthony — U202319057<br>
          Payano Puchuri, Joan Fabricio — U202318620<br>
          Mantilla Maldonado, Enrique Manuel — U20231B842<br>
          Carhuayal Suarez, Joan Salvador — U202219040
        </td>
    </tr>
    <tr align="center">
        <td><strong>Sprint 1 Review Summary</strong></td>
        <td>Se completó y desplegó satisfactoriamente la Landing Page informativa en GitHub Pages, validando el diseño responsive, la coherencia de estilos y la funcionalidad multidioma (inglés/español). La retroalimentación inicial destacó una navegación limpia y clara presentación de la propuesta de valor.</td>
    </tr>
    <tr align="center">
        <td><strong>Sprint 1 Retrospective Summary</strong></td>
        <td>Se acordó establecer un desacoplamiento estricto por Bounded Contexts para el desarrollo de la aplicación web, evitando ramas monolíticas. Asimismo, se determinó el uso obligatorio de PrimeVue para componentes visuales complejos y la estandarización de mensajes de commit en formato Conventional Commits en inglés imperativo.</td>
    </tr>
    <tr>
        <td colspan="2" align="center" style="background-color: #eaeaea;"><strong>Sprint Goal &amp; User Stories</strong></td>
    </tr>
    <tr>
        <td align="center"><strong>Sprint 2 Goal</strong></td>
        <td>Our focus is on developing, integrating, and deploying the FullTank Web Application frontend in Vue 3 and PrimeVue structured by independent Bounded Contexts (IAM, Ordering, Catalog, Fulfillment, Inventory, Equipment, Payment, Notification, and Reporting &amp; Analytics). We believe it delivers reactive operational workflows for fuel-requesting companies and fuel suppliers supported by automated unit tests. This will be confirmed when both user segments can authenticate and execute the core demo workflows in production without console errors.</td>
    </tr>
    <tr align="center">
        <td><strong>Sprint 2 Velocity</strong></td>
        <td>50</td>
    </tr>
    <tr align="center">
        <td><strong>Sum of Story Points</strong></td>
        <td>66 *(25 historias planificadas; supera la velocidad estimada en 16 SP)*</td>
    </tr>
</table>

##### Historias de Usuario Planificadas en el Sprint 2

| ID | Título de la Historia de Usuario | Descripción Resumida | Story Points |
| :--- | :--- | :--- | :---: |
| **US-15** | Iniciar sesión | Autenticación segura de usuarios mediante credenciales y redirección por rol. | 2 |
| **US-40** | Registrar empresa solicitante | Formulario de alta para empresas consumidoras con datos fiscales (RUC) y de contacto. | 3 |
| **US-41** | Registrar empresa proveedora | Registro corporativo de distribuidoras de combustible con descripción y catálogo. | 3 |
| **US-16** | Recuperar contraseña | Solicitud y flujo de restablecimiento de contraseña de acceso. | 2 |
| **US-17** | Cerrar sesión | Cierre seguro de sesión invalidando tokens locales y limpiando el estado. | 1 |
| **US-23** | Ver perfil de usuario | Consulta de datos generales de la empresa y del representante registrado. | 1 |
| **US-24** | Editar datos de perfil | Actualización de datos de contacto, dirección y configuración de la cuenta. | 2 |
| **US-05** | Registrar nuevo pedido | Formulario reactivo para solicitar combustible especificando tipo, cantidad y ubicación. | 5 |
| **US-06** | Consultar estado del pedido | Visualización del estado en tiempo real de los pedidos activos del solicitante. | 2 |
| **US-43** | Ver detalle de pedido | Vista detallada con desglose de montos, proveedor, fecha y trazabilidad de entrega. | 2 |
| **US-10** | Ver pedidos pendientes | Bandeja de entrada del proveedor con solicitudes por evaluar y procesar. | 2 |
| **US-11** | Aprobar pedido | Acción del proveedor para aceptar una solicitud de combustible y pasar a preparación. | 3 |
| **US-42** | Rechazar pedido | Rechazo justificado de solicitudes por falta de cobertura o stock insuficiente. | 2 |
| **US-46** | Gestionar inventario de combustibles | Registro, actualización de stock y edición de precios de los productos ofrecidos. | 3 |
| **US-44** | Gestionar vehículos de flota | Administración de camiones cisterna con placas y capacidades en galones/litros. | 3 |
| **US-45** | Gestionar conductores | Registro de operadores de transporte con licencias y datos de contacto. | 3 |
| **US-49** | Asignar recursos a despacho | Vinculación en un paso de vehículo cisterna y conductor a una orden aprobada. | 5 |
| **US-08** | Registrar información de pago | Adjuntar comprobante de transferencia bancaria y código de operación. | 3 |
| **US-29** | Recibir notificación de aprobación | Alertas visuales ante cambios de estado de las órdenes solicitadas. | 2 |
| **US-30** | Notificación de pedido despachado | Notificación al cliente indicando salida del camión cisterna a destino. | 2 |
| **US-47** | Ver Dashboard principal del proveedor | Métricas clave de rendimiento (KPIs), pedidos activos y tendencias de venta. | 3 |
| **US-18** | Ver resumen de pedidos (Solicitante) | Panel del solicitante con indicadores de volumen solicitado y órdenes en curso. | 3 |
| **US-33** | Ver gráfico de consumo (Solicitante) | Visualización gráfica del consumo histórico mensual de combustible. | 3 |
| **US-34** | Ver gráfico de ventas (Proveedor) | Visualización gráfica de ingresos y volumen despachado por período. | 3 |
| **US-35** | Descargar reporte PDF | Exportación de reportes de gestión en formato PDF estructurado. | 3 |
| **Total** | **25 Historias de Usuario Planificadas** | — | **66 SP** |

El total planificado comprende 66 Story Points distribuidos en las 25 historias seleccionadas para el frontend en el Sprint 2.

---

#### 5.2.2.2. Aspect Leaders and Collaborators

En el Sprint 2 el alcance funcional del frontend se dividió en doce aspectos técnicos correspondientes a la base compartida (`Shared`), los nueve Bounded Contexts de negocio (`IAM`, `Catalog`, `Ordering`, `Equipment`, `Inventory`, `Fulfillment`, `Notifications`, `Payment`, `Reporting & Analytics`), las pruebas unitarias (`Unit Testing & QA`) y el despliegue continuo (`CI/CD & Deployment`). Para cada aspecto se asignó un líder (`L`) responsable del diseño e integración del módulo y colaboradores (`C`) para soporte, pruebas y revisión cruzada de Pull Requests.

<table border="1" cellpadding="6" cellspacing="0" style="border-collapse: collapse; width: 100%;">
    <thead>
        <tr align="center" style="background-color: #f2f2f2;">
            <th>Team Member<br>(Last Name, First Name)</th>
            <th>GitHub Username</th>
            <th>Shared Base<br>Leader (L) / Collaborator (C)</th>
            <th>IAM<br>Leader (L) / Collaborator (C)</th>
            <th>Catalog<br>Leader (L) / Collaborator (C)</th>
            <th>Ordering<br>Leader (L) / Collaborator (C)</th>
            <th>Equipment<br>Leader (L) / Collaborator (C)</th>
            <th>Inventory<br>Leader (L) / Collaborator (C)</th>
            <th>Fulfillment<br>Leader (L) / Collaborator (C)</th>
            <th>Notifications<br>Leader (L) / Collaborator (C)</th>
            <th>Payment<br>Leader (L) / Collaborator (C)</th>
            <th>Reporting<br>Leader (L) / Collaborator (C)</th>
            <th>Testing &amp; QA<br>Leader (L) / Collaborator (C)</th>
            <th>CI/CD &amp; Deploy<br>Leader (L) / Collaborator (C)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Corvacho Damian, Brayan Alexis</td>
            <td>BralexCD</td>
            <td align="center"><strong>L</strong></td>
            <td align="center"><strong>L</strong></td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center"><strong>L</strong></td>
            <td align="center"><strong>L</strong></td>
        </tr>
        <tr>
            <td>Mantilla Maldonado, Enrique Manuel</td>
            <td>enrique-mantilla</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center"><strong>L</strong></td>
            <td align="center"><strong>L</strong></td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
        </tr>
        <tr>
            <td>Carhuayal Suarez, Joan Salvador</td>
            <td>JoanCS</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center"><strong>L</strong></td>
            <td align="center"><strong>L</strong></td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
        </tr>
        <tr>
            <td>Huingo Tello, Frank Anthony</td>
            <td>Franz2308</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center"><strong>L</strong></td>
            <td align="center"><strong>L</strong></td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
        </tr>
        <tr>
            <td>Payano Puchuri, Joan Fabricio</td>
            <td>joanfpp2-ai</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center"><strong>L</strong></td>
            <td align="center"><strong>L</strong></td>
            <td align="center">C</td>
            <td align="center">C</td>
        </tr>
    </tbody>
</table>

*Nota de revisión cruzada:* Las revisiones por pares de los Pull Requests se realizaron de forma cruzada entre los líderes de arquitectura (`BralexCD`), dominio (`enrique-mantilla`, `Franz2308`) y módulos de soporte (`JoanCS`, `joanfpp2-ai`).

---

#### 5.2.2.3. Sprint Backlog 2

El objetivo principal del Sprint 2 es implementar, integrar y desplegar la primera versión funcional de la Web Application de FullTank en Vue 3 y PrimeVue organizada por Bounded Contexts independientes, cubriendo los flujos operativos de compradores y proveedores de combustible mediante adaptadores demo y pruebas unitarias automatizadas.

**Tablero del Sprint Backlog:** [FullTank · FuelPoint | Product Backlog y Sprints · TB1](https://trello.com/b/6h5mZ8L6).

La [captura y nota de alcance en 3.3 Product Backlog](chapter3.md#33-product-backlog) muestran el tablero del Sprint 2: 34 historias en Hecho y 17 en Product Backlog.

A continuación se detalla la desagregación de las Historias de Usuario en tareas técnicas (*Sprint Backlog*) para el Sprint 2:

<table border="1" cellpadding="6" cellspacing="0" style="border-collapse: collapse; width: 100%;">
    <tr align="center" style="background-color: #f2f2f2;">
        <td colspan="2"><strong>Sprint #</strong></td>
        <td colspan="6"><strong>Sprint 2</strong></td>
    </tr>
    <tr align="center" style="background-color: #eaeaea;">
        <td colspan="2"><strong>User Story</strong></td>
        <td colspan="6"><strong>Work-Item / Task</strong></td>
    </tr>
    <tr align="center" style="background-color: #f9f9f9;">
        <td><strong>Story Id</strong></td>
        <td><strong>Story Title</strong></td>
        <td><strong>Task Id</strong></td>
        <td><strong>Task Title</strong></td>
        <td><strong>Task Description</strong></td>
        <td><strong>Estimation (Hours)</strong></td>
        <td><strong>Assigned To</strong></td>
        <td><strong>Status (To-do / In-Process / To-Review / Done)</strong></td>
    </tr>
    <tr>
        <td align="center">US-39</td>
        <td>Cambiar idioma</td>
        <td align="center">TSK-201</td>
        <td>Base Vue 3, PrimeVue e i18n</td>
        <td>Inicializar proyecto Vue 3 con Vite, configurar PrimeVue 4, PrimeFlex e i18n multidioma (en_US / es_419).</td>
        <td align="center">6</td>
        <td>Brayan Corvacho</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">US-15</td>
        <td>Iniciar sesión</td>
        <td align="center">TSK-202</td>
        <td>Stores Pinia y cliente HTTP Axios</td>
        <td>Configurar stores base e interceptores de autenticación sobre cliente HTTP centralizado Axios.</td>
        <td align="center">5</td>
        <td>Brayan Corvacho</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">US-15, US-40, US-41</td>
        <td>Iniciar sesión / Registrar empresa solicitante y proveedora</td>
        <td align="center">TSK-203</td>
        <td>Vistas de Sign-in y Sign-up por rol</td>
        <td>Desarrollar vistas de acceso y registro corporativo con selección de rol (Comprador / Proveedor).</td>
        <td align="center">8</td>
        <td>Brayan Corvacho</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">US-23, US-24</td>
        <td>Ver y editar perfil de usuario</td>
        <td align="center">TSK-204</td>
        <td>Vistas de perfil corporativo</td>
        <td>Implementar consulta y edición de datos generales, fiscales y de contacto de la empresa.</td>
        <td align="center">5</td>
        <td>Brayan Corvacho</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">US-15, US-17</td>
        <td>Iniciar sesión / Cerrar sesión</td>
        <td align="center">TSK-205</td>
        <td>Guards de navegación por rol</td>
        <td>Configurar guards en Vue Router para validar sesión activa, rol y cierre seguro de sesión.</td>
        <td align="center">4</td>
        <td>Brayan Corvacho</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">US-16</td>
        <td>Recuperar contraseña</td>
        <td align="center">TSK-226</td>
        <td>Flujo de recuperación de contraseña</td>
        <td>Implementar pantalla y validaciones de solicitud de restablecimiento de contraseña desde login.</td>
        <td align="center">4</td>
        <td>Brayan Corvacho</td>
        <td align="center">To-do</td>
    </tr>
    <tr>
        <td align="center">US-46</td>
        <td>Gestionar inventario de combustibles</td>
        <td align="center">TSK-206</td>
        <td>Catálogo interactivo de combustibles</td>
        <td>Construir catálogo de combustibles y proveedores con tarjetas de especificaciones, precios y filtros.</td>
        <td align="center">6</td>
        <td>Enrique Mantilla</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">US-05</td>
        <td>Registrar nuevo pedido</td>
        <td align="center">TSK-207</td>
        <td>Formulario de solicitud de combustible</td>
        <td>Implementar formulario reactivo de nueva solicitud con selección de combustible y cálculo automático.</td>
        <td align="center">9</td>
        <td>Enrique Mantilla</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">US-06, US-43</td>
        <td>Consultar estado y ver detalle del pedido</td>
        <td align="center">TSK-208</td>
        <td>Trazabilidad y detalle de pedidos</td>
        <td>Desarrollar vista de seguimiento de estado y desglose completo de pedidos del solicitante.</td>
        <td align="center">7</td>
        <td>Enrique Mantilla</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">US-10, US-11, US-42</td>
        <td>Ver pedidos pendientes / Aprobar y rechazar pedido</td>
        <td align="center">TSK-209</td>
        <td>Bandeja de evaluación del proveedor</td>
        <td>Implementar bandeja de solicitudes entrantes para el proveedor con acciones de aprobar y rechazar.</td>
        <td align="center">8</td>
        <td>Enrique Mantilla</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">US-46</td>
        <td>Gestionar inventario de combustibles</td>
        <td align="center">TSK-210</td>
        <td>Módulo de inventario de proveedor</td>
        <td>Crear gestión de existencias de tanques con indicadores de stock físico, reservado, disponible y precios.</td>
        <td align="center">7</td>
        <td>Joan Carhuayal</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">US-05</td>
        <td>Registrar nuevo pedido</td>
        <td align="center">TSK-211</td>
        <td>CRUD de equipos del comprador</td>
        <td>Construir interfaz de administración de equipos y maquinaria con diálogos de creación y edición.</td>
        <td align="center">7</td>
        <td>Joan Carhuayal</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">US-05</td>
        <td>Registrar nuevo pedido</td>
        <td align="center">TSK-212</td>
        <td>Integración de equipos al pedido</td>
        <td>Integrar store de equipos y vincular la selección de maquinaria al formulario de solicitud.</td>
        <td align="center">5</td>
        <td>Joan Carhuayal</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">US-44</td>
        <td>Gestionar vehículos de flota</td>
        <td align="center">TSK-213</td>
        <td>Módulo de flota de cisternas</td>
        <td>Desarrollar administración de camiones cisterna del proveedor (placas, tipo, capacidad y estado).</td>
        <td align="center">7</td>
        <td>Frank Huingo</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">US-45</td>
        <td>Gestionar conductores</td>
        <td align="center">TSK-214</td>
        <td>Módulo de conductores</td>
        <td>Desarrollar registro y gestión de operadores de transporte con licencias y datos de contacto.</td>
        <td align="center">6</td>
        <td>Frank Huingo</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">US-49</td>
        <td>Asignar recursos a despacho</td>
        <td align="center">TSK-215</td>
        <td>Modal de asignación a despacho</td>
        <td>Implementar asignación de vehículo cisterna y conductor a pedidos en estado aprobado.</td>
        <td align="center">8</td>
        <td>Frank Huingo</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">US-29, US-30</td>
        <td>Notificaciones de aprobación y despacho</td>
        <td align="center">TSK-216</td>
        <td>Centro de notificaciones reactivo</td>
        <td>Construir feed de alertas con contador de no leídas y disparadores ante cambios de estado.</td>
        <td align="center">5</td>
        <td>Frank Huingo</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">US-08</td>
        <td>Registrar información de pago</td>
        <td align="center">TSK-217</td>
        <td>Formulario de pago y comprobante</td>
        <td>Implementar interfaz de pago demo y generación de comprobante académico en el módulo Payment.</td>
        <td align="center">7</td>
        <td>Joan Payano</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">US-08, US-11</td>
        <td>Registrar pago / Aprobar pedido</td>
        <td align="center">TSK-218</td>
        <td>Historial y verificación de comprobantes</td>
        <td>Desarrollar vista de historial y consulta de comprobantes asociados a órdenes pagadas.</td>
        <td align="center">6</td>
        <td>Joan Payano</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">US-33, US-18</td>
        <td>Ver gráfico de consumo y resumen de pedidos</td>
        <td align="center">TSK-219</td>
        <td>Analítica de consumo del comprador</td>
        <td>Integrar dashboard y gráficos de consumo mensual por combustible y equipo usando Chart.js.</td>
        <td align="center">7</td>
        <td>Joan Payano</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">US-34, US-47</td>
        <td>Ver gráfico de ventas y Dashboard del proveedor</td>
        <td align="center">TSK-220</td>
        <td>Dashboard y analítica del proveedor</td>
        <td>Construir panel principal del proveedor con KPIs, ingresos mensuales y distribución de ventas.</td>
        <td align="center">8</td>
        <td>Joan Payano</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">US-35</td>
        <td>Descargar reporte PDF</td>
        <td align="center">TSK-221</td>
        <td>Exportación de reportes PDF</td>
        <td>Implementar servicio de exportación y descarga de resúmenes de operación analítica en formato PDF.</td>
        <td align="center">6</td>
        <td>Joan Payano</td>
        <td align="center">To-do</td>
    </tr>
    <tr>
        <td align="center">US-15, US-08</td>
        <td>Iniciar sesión / Registrar pago</td>
        <td align="center">TSK-222</td>
        <td>Pruebas unitarias con Vitest</td>
        <td>Escribir suite de pruebas automatizadas con Vitest para stores, validaciones y adaptadores API.</td>
        <td align="center">6</td>
        <td>Brayan Corvacho</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">Technical Support</td>
        <td>Integración continua (CI/CD)</td>
        <td align="center">TSK-223</td>
        <td>Pipeline CI/CD en GitHub Actions</td>
        <td>Configurar workflow automatizado de instalación, ejecución de pruebas Vitest y compilación demo.</td>
        <td align="center">4</td>
        <td>Brayan Corvacho</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">Technical Support</td>
        <td>Despliegue en la nube</td>
        <td align="center">TSK-224</td>
        <td>Publicación en Firebase Hosting</td>
        <td>Desplegar Web Application en Firebase Hosting (`full-tank-964e2.web.app`) con reescritura SPA verificada.</td>
        <td align="center">4</td>
        <td>Brayan Corvacho</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">US-05, US-10</td>
        <td>Registrar pedido / Ver pedidos pendientes</td>
        <td align="center">TSK-225</td>
        <td>Pruebas de responsividad móvil</td>
        <td>Ejecutar pruebas visuales de usabilidad y diseño adaptable en resoluciones móvil y escritorio.</td>
        <td align="center">5</td>
        <td>Frank Huingo</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td colspan="5" align="right"><strong>Total Estimated Hours (Sprint 2)</strong></td>
        <td align="center"><strong>160</strong></td>
        <td colspan="2"></td>
    </tr>
</table>

---

#### 5.2.2.4. Development Evidence for Sprint Review

**Repositorio oficial:** [Full_Tank_Frontend](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend).

Durante el Sprint 2 se implementó la arquitectura modular del frontend en ramas temáticas por Bounded Context, integradas hacia `develop` y liberadas en `main` mediante Pull Requests (#2 al #11) bajo el tag `v1.0.0`. A continuación se presentan los commits verificados por rama en el repositorio oficial:

<table border="1" cellpadding="6" cellspacing="0" style="border-collapse: collapse; width: 100%;">
    <thead>
        <tr align="center" style="background-color: #f2f2f2;">
            <th>Repository</th>
            <th>Branch</th>
            <th>Commit Id</th>
            <th>Commit Message</th>
            <th>Commit Message Body</th>
            <th>Commited on (Date)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend</td>
            <td>feat/shared</td>
            <td>2adc9d1</td>
            <td>feat(shared): incorporar base minima independiente de los BC</td>
            <td>Configuración inicial de Vite, Vue 3, PrimeVue, i18n, router base y capa compartida.</td>
            <td>2026-10-09</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend</td>
            <td>feat/iam</td>
            <td>d4ee176</td>
            <td>feat(iam): import session domain model</td>
            <td>Definición de entidades de usuario, empresa compradora/proveedora y sesión.</td>
            <td>2026-10-09</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend</td>
            <td>feat/iam</td>
            <td>24f7203</td>
            <td>feat(iam): implement demo authentication and company APIs</td>
            <td>Adaptadores API demo para inicio de sesión, registro corporativo y perfiles.</td>
            <td>2026-10-09</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend</td>
            <td>feat/iam</td>
            <td>81f0975</td>
            <td>feat(iam): integrate session and profile store</td>
            <td>Store Pinia para gestión de estado de autenticación, rol y perfil de usuario.</td>
            <td>2026-10-09</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend</td>
            <td>feat/iam</td>
            <td>b856edb</td>
            <td>feat(iam): add authentication views and route guards</td>
            <td>Vistas de login, registro por segmento y guards de navegación por rol.</td>
            <td>2026-10-09</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend</td>
            <td>feat/fulfillment</td>
            <td>43c04be</td>
            <td>feat(fulfillment): define driver and vehicle domain entities</td>
            <td>Modelos de dominio para conductores, camiones cisterna y entregas.</td>
            <td>2026-10-08</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend</td>
            <td>feat/fulfillment</td>
            <td>1751254</td>
            <td>feat(fulfillment): implement driver and vehicle views and routing</td>
            <td>Vistas de administración de flota y conductores con rutas de proveedor.</td>
            <td>2026-10-08</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend</td>
            <td>feat/notification</td>
            <td>21eeea6</td>
            <td>feat(notification): define notification domain entity and value types</td>
            <td>Definición de entidades de alerta, tipos de evento y estados de lectura.</td>
            <td>2026-10-08</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend</td>
            <td>feat/notification</td>
            <td>d5bbbd3</td>
            <td>feat(notification): add notification list view and register routes</td>
            <td>Vista del centro de notificaciones y registro de rutas por segmento.</td>
            <td>2026-10-09</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend</td>
            <td>feat/notification</td>
            <td>e9717cb</td>
            <td>test(notification): cover store actions and unread badge count</td>
            <td>Pruebas unitarias Vitest sobre acciones de lectura y contador de alertas.</td>
            <td>2026-10-09</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend</td>
            <td>feat/equipment</td>
            <td>0e6ce9e</td>
            <td>feat(equipment): import equipment domain model and entity</td>
            <td>Modelo de dominio para maquinaria, generadores y tanques del comprador.</td>
            <td>2026-10-08</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend</td>
            <td>feat/equipment</td>
            <td>b1f8e9c</td>
            <td>feat(equipment): add client equipment views and register routes</td>
            <td>Interfaz CRUD de equipos con barras de capacidad y pruebas unitarias.</td>
            <td>2026-10-08</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend</td>
            <td>feat/inventory</td>
            <td>f983a3a</td>
            <td>feat(inventory): import product domain model and entity</td>
            <td>Modelo de dominio para productos de combustible y movimientos de inventario.</td>
            <td>2026-10-08</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend</td>
            <td>feat/inventory</td>
            <td>4561913</td>
            <td>feat(inventory): add stock management views and register routes</td>
            <td>Vistas de control de stock físico, reservado y alertas de reposición.</td>
            <td>2026-10-09</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend</td>
            <td>feat/catalog</td>
            <td>b189375</td>
            <td>feat(catalog): added two entities</td>
            <td>Entidades de catálogo de combustibles y directorio de proveedores.</td>
            <td>2026-10-09</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend</td>
            <td>feat/catalog</td>
            <td>a05238f</td>
            <td>feat(catalog): added presentation</td>
            <td>Vistas de exploración de catálogo, detalle de proveedor y panel de solicitud.</td>
            <td>2026-10-09</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend</td>
            <td>feat/ordering</td>
            <td>bba2b43</td>
            <td>feat(ordering): added order and request entity</td>
            <td>Modelos de dominio para solicitudes de combustible y ciclo de vida de órdenes.</td>
            <td>2026-10-09</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend</td>
            <td>feat/ordering</td>
            <td>932360c</td>
            <td>fix(ordering): standardize store filename and add store unit tests</td>
            <td>Estandarización de store de órdenes, vistas de flujo y pruebas unitarias.</td>
            <td>2026-10-09</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend</td>
            <td>feat/payment</td>
            <td>1778e2d</td>
            <td>feat(payment): import payment and invoice domain entities</td>
            <td>Entidades de dominio para pagos y comprobantes académicos del sistema.</td>
            <td>2026-10-08</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend</td>
            <td>feat/payment</td>
            <td>e6c62b3</td>
            <td>fix(payment): add missing invoice document component and store tests</td>
            <td>Componente de comprobante, diálogo de pago demo y pruebas unitarias.</td>
            <td>2026-10-09</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend</td>
            <td>feat/reporting</td>
            <td>9827194</td>
            <td>feat(reporting): import financial period domain helpers</td>
            <td>Helpers de dominio para agrupación de métricas por períodos financieros.</td>
            <td>2026-10-08</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend</td>
            <td>feat/reporting</td>
            <td>375f4be</td>
            <td>feat(reporting): add buyer and provider analytics views and register routes</td>
            <td>Dashboards de analítica y gráficos para comprador y proveedor.</td>
            <td>2026-10-09</td>
        </tr>
    </tbody>
</table>

##### Resumen de Pull Requests integrados (Sprint 2)

| Pull Request | Rama | SHA de cabeza | Cuenta autora | Título publicado | Estado verificado |
|---|---|---|---|---|---|
| [#1](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend/pull/1) | `feat/frontend-title-i18n` | `7c2c47a` | `BralexCD` | feat: titulo FullTank y docs demo | Cerrado sin integrar |
| [#2](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend/pull/2) | `feat/shared` | `2adc9d1` | `BralexCD` | feat(shared): incorporar base minima de FullTank | Integrado |
| [#3](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend/pull/3) | `feat/iam` | `b856edb` | `BralexCD` | feat(iam): add demo authentication and session management | Integrado |
| [#4](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend/pull/4) | `feat/fulfillment` | `1751254` | `Franz2308` | feat(fulfillment): fleet and driver logistics management | Integrado |
| [#5](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend/pull/5) | `feat/notification` | `e9717cb` | `Franz2308` | feat(notification): alert center, unread counter, and reactive toast triggers | Integrado |
| [#6](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend/pull/6) | `feat/equipment` | `b1f8e9c` | `JoanCS` | feat(equipment): client machinery and fuel tank monitoring | Integrado |
| [#7](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend/pull/7) | `feat/inventory` | `4561913` | `JoanCS` | feat(inventory): supplier fuel tank stock and alert thresholds | Integrado |
| [#8](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend/pull/8) | `feat/catalog` | `a05238f` | `enrique-mantilla` | feat(catalog): product catalog, provider directory and fuel request panel | Integrado |
| [#9](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend/pull/9) | `feat/ordering` | `932360c` | `enrique-mantilla` | feat(ordering): fuel orders, requests lifecycle and dispatch management | Integrado |
| [#10](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend/pull/10) | `feat/payment` | `e6c62b3` | `joanfpp2-ai` | feat(payment): invoice registry, payment verification and voucher upload | Integrado |
| [#11](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend/pull/11) | `feat/reporting` | `375f4be` | `joanfpp2-ai` | feat(reporting): buyer and provider analytics dashboards and KPI metrics | Integrado |

Los diez Pull Requests (#2 al #11) correspondientes a la base compartida y a cada uno de los Bounded Contexts fueron integrados de forma satisfactoria hacia `develop` y posteriormente liberados en `main` bajo el tag de release `v1.0.0`.

**Relación con el despliegue:** la demo integrada está disponible en Firebase Hosting y fue recorrida para las capturas de 5.2.2.5. El repositorio oficial cuenta con un pipeline de CI/CD automatizado en GitHub Actions que ejecuta pruebas unitarias y despliega a producción en cada push.

**Evidencia conservada:** [consulta de Pull Requests](../assets/chapter-5/ejecucion-tb1/github-pull-requests.json) y [registro de verificación](../assets/chapter-5/ejecucion-tb1/VERIFICACION_TB1.md).

---

#### 5.2.2.5. Execution Evidence for Sprint Review

La aplicación desplegada en [Firebase Hosting](https://full-tank-964e2.web.app/iam/login) fue recorrida el **9 de octubre de 2026**, con las cuentas demo de comprador y proveedor. Las imágenes siguientes son capturas de la aplicación publicada, sin sustituir pantallas por mockups. Resoluciones: **1440 × 1000 px** en escritorio y **390 × 844 px** en móvil.

**Alcance:** primera versión del frontend con API simulada en memoria. Las empresas, pedidos y valores mostrados son datos demo; sus fechas no representan la fecha de esta verificación. Los pagos son simulados. Las capturas acreditan acceso y visualización de las pantallas descritas; no certifican todas las operaciones CRUD ni una integración con backend productivo.

> **Grabación de Sustentación y Recorrido de la Aplicación Web (TB1):**  
> [Ver exposición TB1 en Microsoft Stream](https://upcedupe-my.sharepoint.com/:v:/g/personal/u20231a257_upc_edu_pe/IQBOLr6orh8kSYVocJuNA4awAZE_KVDNpkV2wqSCSsXiDLU?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D&e=7koIIx)
> *(Archivo: `upc-pre-202620-1asi0730-16129-fuelpoint-expo-tb1.mp4`. Duración: **21:39**, confirmada en la captura del reproductor proporcionada por el equipo; cumple el máximo de 30 minutos).*

La captura del reproductor confirma el nombre del archivo y la duración de la exposición TB1. El contenido completo y los permisos del evaluador no se verificaron desde el acceso público. Las capturas de la aplicación de esta sección se obtuvieron directamente del despliegue.

##### 1. Autenticación y registro

Se comprobó el ingreso de las dos cuentas demo y el cierre de sesión. El registro muestra la selección entre comprador y proveedor. La recuperación de contraseña (US-16) sigue pendiente. El texto de marca «PrimeFuel» aún visible en el login/registro proviene de la versión desplegada y debe actualizarse a FuelPoint en una siguiente publicación.

<div align="center">
  <img src="../assets/chapter-5/ejecucion-tb1/login-desktop.png" alt="Acceso real a FullTank y credenciales de demostración, vista de escritorio." width="850"/>
  <p><em>Acceso real a FullTank y credenciales de demostración, vista de escritorio.</em></p>
</div>
<div align="center">
  <img src="../assets/chapter-5/ejecucion-tb1/login-mobile.png" alt="Inicio de sesión en el despliegue, vista móvil." width="300"/>
  <p><em>Inicio de sesión en el despliegue, vista móvil.</em></p>
</div>
<div align="center">
  <img src="../assets/chapter-5/ejecucion-tb1/registro-mobile.png" alt="Formulario real de registro, vista móvil; no se creó una cuenta durante la revisión." width="300"/>
  <p><em>Formulario real de registro, vista móvil; no se creó una cuenta durante la revisión.</em></p>
</div>

##### 2. Segmento comprador / solicitante

Se consultaron el dashboard, catálogo de proveedores, equipos y solicitudes. La creación de una nueva solicitud comienza desde el catálogo. Se capturaron los estados de las solicitudes precargadas y las alertas de los equipos.

<div align="center">
  <img src="../assets/chapter-5/ejecucion-tb1/buyer-dashboard-desktop.png" alt="Dashboard del comprador con indicadores y órdenes precargadas." width="850"/>
  <p><em>Dashboard del comprador con indicadores y órdenes precargadas.</em></p>
</div>
<div align="center">
  <img src="../assets/chapter-5/ejecucion-tb1/catalogo-desktop.png" alt="Catálogo real de proveedores y combustibles de la demo." width="850"/>
  <p><em>Catálogo real de proveedores y combustibles de la demo.</em></p>
</div>
<div align="center">
  <img src="../assets/chapter-5/ejecucion-tb1/equipos-desktop.png" alt="Equipos del comprador con capacidad y nivel de combustible." width="850"/>
  <p><em>Equipos del comprador con capacidad y nivel de combustible.</em></p>
</div>
<div align="center">
  <img src="../assets/chapter-5/ejecucion-tb1/nueva-solicitud-desktop.png" alt="Formulario real de solicitud desde el detalle del proveedor" width="850"/>
  <p><em>Formulario de solicitud del proveedor con selección de combustible, equipo, cantidad, dirección y fecha. No se envió una solicitud durante la revisión.</em></p>
</div>

<div align="center">
  <img src="../assets/chapter-5/ejecucion-tb1/solicitudes-desktop.png" alt="Listado real de solicitudes y sus estados." width="850"/>
  <p><em>Listado real de solicitudes y sus estados.</em></p>
</div>
<div align="center">
  <img src="../assets/chapter-5/ejecucion-tb1/buyer-dashboard-mobile.png" alt="Dashboard del comprador en móvil con la barra lateral contraída." width="300"/>
  <p><em>Dashboard del comprador en móvil con la barra lateral contraída.</em></p>
</div>
<div align="center">
  <img src="../assets/chapter-5/ejecucion-tb1/equipos-mobile.png" alt="Consulta de equipos en móvil con navegación contraída." width="300"/>
  <p><em>Consulta de equipos en móvil con navegación contraída.</em></p>
</div>

##### 3. Segmento proveedor / distribuidor

Se accedió con `dispatch@petroandes.com` y se consultaron el dashboard, las solicitudes pendientes con acciones de aceptar/rechazar, inventario, flota y conductores. Estas capturas registran la consulta; no se efectuó un despacho durante esta revisión.

<div align="center">
  <img src="../assets/chapter-5/ejecucion-tb1/provider-dashboard-desktop.png" alt="Dashboard del proveedor con solicitudes y órdenes de la demo." width="850"/>
  <p><em>Dashboard del proveedor con solicitudes y órdenes de la demo.</em></p>
</div>
<div align="center">
  <img src="../assets/chapter-5/ejecucion-tb1/pendientes-proveedor-desktop.png" alt="Solicitudes pendientes visibles para el proveedor." width="850"/>
  <p><em>Solicitudes pendientes visibles para el proveedor.</em></p>
</div>
<div align="center">
  <img src="../assets/chapter-5/ejecucion-tb1/inventario-desktop.png" alt="Inventario del proveedor con stock físico, reservado y disponible." width="850"/>
  <p><em>Inventario del proveedor con stock físico, reservado y disponible.</em></p>
</div>
<div align="center">
  <img src="../assets/chapter-5/ejecucion-tb1/flota-desktop.png" alt="Flota registrada y estados de los vehículos." width="850"/>
  <p><em>Flota registrada y estados de los vehículos.</em></p>
</div>
<div align="center">
  <img src="../assets/chapter-5/ejecucion-tb1/conductores-desktop.png" alt="Registro de conductores y disponibilidad." width="850"/>
  <p><em>Registro de conductores y disponibilidad.</em></p>
</div>
<div align="center">
  <img src="../assets/chapter-5/ejecucion-tb1/provider-dashboard-mobile.png" alt="Dashboard del proveedor en móvil con navegación contraída." width="300"/>
  <p><em>Dashboard del proveedor en móvil con navegación contraída.</em></p>
</div>

##### 4. Pagos simulados

La vista muestra órdenes pendientes y permite abrir el formulario de pago demo con opciones Card/Yape. Se verificó la apertura del formulario, sin confirmar un pago ni ingresar datos financieros reales. La versión observada no corresponde al flujo de carga de comprobante bancario descrito en la planificación de US-08; ese criterio debe revisarse con el equipo antes de cerrar la historia.

<div align="center">
  <img src="../assets/chapter-5/ejecucion-tb1/pagos-desktop.png" alt="Órdenes pendientes de pago en la demo académica." width="850"/>
  <p><em>Órdenes pendientes de pago en la demo académica.</em></p>
</div>
<div align="center">
  <img src="../assets/chapter-5/ejecucion-tb1/pago-demo-desktop.png" alt="Formulario de pago simulado abierto desde la aplicación desplegada." width="850"/>
  <p><em>Formulario de pago simulado abierto desde la aplicación desplegada.</em></p>
</div>

##### 5. Reportes y notificaciones

Se consultaron los reportes del comprador y proveedor, sus filtros de periodo y los gráficos de gasto/ingreso. Se visualizó el historial de notificaciones precargadas. No se encontró una acción de exportación PDF en estas pantallas; **US-35 y TSK-221 siguen pendientes**.

<div align="center">
  <img src="../assets/chapter-5/ejecucion-tb1/reportes-comprador-desktop.png" alt="Reporte del comprador con gráficos de gasto y desglose por equipo." width="850"/>
  <p><em>Reporte del comprador con gráficos de gasto y desglose por equipo.</em></p>
</div>
<div align="center">
  <img src="../assets/chapter-5/ejecucion-tb1/reportes-proveedor-desktop.png" alt="Reporte del proveedor con ingresos, órdenes y clientes." width="850"/>
  <p><em>Reporte del proveedor con ingresos, órdenes y clientes.</em></p>
</div>
<div align="center">
  <img src="../assets/chapter-5/ejecucion-tb1/notificaciones-desktop.png" alt="Centro de notificaciones con eventos precargados de la demo." width="850"/>
  <p><em>Centro de notificaciones con eventos precargados de la demo.</em></p>
</div>

##### 6. Verificación de responsividad

Login y registro se abrieron a 390 × 844 px. En las vistas internas se utilizó el botón de menú para contraer la barra lateral; con la barra expandida se reduce considerablemente el espacio del contenido. Queda pendiente mejorar su comportamiento automático en móvil y validar tablas extensas a 375 px. No se declara una validación completa de accesibilidad ni responsividad a partir de estas capturas.

---

#### 5.2.2.6. Services Documentation Evidence for Sprint Review

Para TB1 se utiliza la **API simulada en memoria** (`VITE_USE_FAKE_API=true`) detrás del cliente Axios. Los contratos siguientes se contrastaron con los adaptadores de la demo integrada y `.env.demo`, con base `/api/v1`. Son contratos de integración del frontend; no indican que exista un backend ASP.NET Core desplegado.

| Contexto | Método | Ruta relativa a `/api/v1` | Operación y entrada |
|---|---|---|---|
| IAM | POST | `/authentication/sign-in` | Inicio de sesión: `{ email, password }`. |
| IAM | POST | `/authentication/sign-up` | Registro de usuario vinculado a empresa; datos definidos por el formulario y adaptador. |
| IAM | GET | `/users/{id}` | Consulta del usuario por identificador. |
| IAM | PUT | `/users/{id}/profile` | Actualización del perfil. |
| IAM | PUT | `/users/{id}/password` | Cambio de contraseña: `{ currentPassword, newPassword }`. |
| IAM | GET / POST | `/buyer-companies`, `/provider-companies` | Directorios y creación de empresas de cada segmento. |
| Catalog | GET | `/provider-companies`, `/inventory-items` | Catálogo proyectado desde los proveedores y su inventario. |
| Catalog | GET / POST | `/favorite-providers` | Consulta por `companyId` y registro de favoritos. |
| Catalog | GET / POST / PUT | `/provider-ratings`, `/provider-ratings/{id}` | Consulta, creación y edición de valoraciones. |
| Ordering | GET / POST | `/fuel-requests` | Consulta y creación de solicitudes. |
| Ordering | POST | `/fuel-requests/{id}/approve` | Aprobar una solicitud con cuerpo `{}`. |
| Ordering | GET / POST / PUT / DELETE | `/orders`, `/orders/{id}` | Operaciones sobre órdenes mediante el adaptador CRUD. |
| Ordering | POST | `/orders/{id}/dispatch` | Asignación de despacho: `{ driverId, vehicleId }`. |
| Ordering | POST | `/orders/{id}/receive` | Confirmar recepción con cuerpo `{}`. |
| Ordering | POST | `/orders/{id}/cancel` | Cancelar una orden: `{ reason }`. |
| Equipment | GET / POST / PUT / DELETE | `/equipment`, `/equipment/{id}` | Consulta y administración de equipos. |
| Equipment | GET / POST | `/refill-history` | Consulta y registro del historial de recargas. |
| Inventory | GET / POST / PUT / DELETE | `/inventory-items`, `/inventory-items/{id}` | Existencias, precios y administración de productos. |
| Inventory | GET / POST | `/inventory-movements` | Consulta y registro de movimientos de stock. |
| Fulfillment | GET | `/vehicles/provider/{providerId}`, `/drivers/provider/{providerId}` | Recursos logísticos del proveedor. |
| Fulfillment | POST / PUT / DELETE | `/vehicles`, `/vehicles/{id}`, `/drivers`, `/drivers/{id}` | Registro, modificación y eliminación de vehículos/conductores. |
| Fulfillment | POST | `/deliveries/{id}/complete` | Completar una entrega desde su adaptador. |
| Payment | GET / POST | `/payments`, `/invoices` | Consulta y creación de pagos/facturas simulados. |
| Payment | POST | `/payment-checkout` | Checkout demo: `{ payment, invoice }`; sin transacción monetaria. |
| Notification | GET / POST | `/notifications` | Consulta y creación de notificaciones. |
| Notification | POST | `/notifications/{id}/read` | Marcar una notificación como leída. |
| Notification | POST | `/notifications/buyer/{id}/read-all`, `/notifications/provider/{id}/read-all` | Marcar todas como leídas por segmento. |
| Reporting | GET | `/analytics/buyer-dashboard/{companyId}`, `/analytics/provider-dashboard/{providerId}` | Indicadores de dashboard. |
| Reporting | GET | `/analytics/buyer/{companyId}/{recurso}` | `spending-summary`, `monthly-spending`, `spending-by-provider`, `spending-by-fuel-type`, `spending-by-equipment`; parámetros de periodo. |
| Reporting | GET | `/analytics/provider/{providerId}/{recurso}` | `sales-summary`, `revenue-over-time`, `revenue-by-fuel-type`, `orders-by-status`, `customers-by-sector`, `top-customers`; parámetros de periodo. |

Las respuestas, validaciones y casos de error de la simulación se verifican en la suite de pruebas unitarias con Vitest (14 archivos de prueba, 90 pruebas automatizadas), junto con las pruebas de stores y coordinación transversal. La definición OpenAPI del backend y sus pruebas de integración corresponden a los siguientes sprints. No se atribuyen códigos HTTP o cuerpos no contrastados al servicio productivo.

---

#### 5.2.2.7. Software Deployment Evidence for Sprint Review

- **Alojamiento:** Firebase Hosting, proyecto `full-tank-964e2`.
- **Acceso público en producción:** [https://full-tank-964e2.web.app/](https://full-tank-964e2.web.app/) ([Iniciar sesión](https://full-tank-964e2.web.app/iam/login)).
- **Repositorio de contribuciones:** [Full_Tank_Frontend](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend).
- **Verificación:** 9 de octubre de 2026; respuesta HTTP 200, ingreso con ambos roles y consulta de las pantallas documentadas en 5.2.2.5.
- **Alcance:** frontend SPA con API simulada en memoria y pagos demo. No se presenta este alojamiento como despliegue de backend.

##### Configuración de publicación y pipeline CI/CD

El proyecto integrado contiene `firebase.json` con `hosting.public: "dist"` y la reescritura `source: "**"`, `destination: "/index.html"`. `.firebaserc` identifica `full-tank-964e2`.

La automatización de compilación, ejecución de pruebas y despliegue continuo se gestiona mediante **GitHub Actions** a través del workflow `.github/workflows/ci-cd.yml`:
- **Disparadores (triggers):** Cada push a las ramas `develop` y `main`.
- **Pipeline automatizado:**
  1. Checkout del código y configuración de Node.js 20 con caché de npm.
  2. Instalación determinista de dependencias con `npm ci`.
  3. Ejecución de pruebas unitarias con `npm test` (Vitest).
  4. Compilación del bundle de producción con `npm run build:demo`.
  5. Despliegue automático a Firebase Hosting mediante `w9j/action-firebase@v2` empleando el secret `FIREBASE_TOKEN`.

Ambas ejecuciones automatizadas concluyeron exitosamente en GitHub Actions (Run ID `37898772687` para `develop` y Run ID `37898773279` para `main`), publicando la versión oficial etiquetada con el release tag `v1.0.0`.

##### Construcción y pruebas verificadas

Tanto en el entorno de desarrollo local como en los runners de GitHub Actions:

- `npm test`: **90/90 pruebas satisfactorias en catorce archivos de prueba** (100% aprobadas), validando IAM, Catalog, Equipment, Inventory, Ordering, Fulfillment, Payment, Reporting, Notification, coordinación entre Bounded Contexts y clientes API.
- `npm run build:demo`: compilación de producción satisfactoria, con salida optimizada en `dist`.
- Despliegue verificado en producción: [https://full-tank-964e2.web.app](https://full-tank-964e2.web.app), retornando código HTTP 200 y título `FullTank`.
- Release oficial: tag `v1.0.0` generado y sincronizado en `origin/main`.

Véanse [resultados de verificación](../assets/chapter-5/ejecucion-tb1/VERIFICACION_TB1.md) y [salida de build](../assets/chapter-5/ejecucion-tb1/build-demo.txt).

---

#### 5.2.2.8. Team Collaboration Insights during Sprint

Resumen:
Durante el Sprint 2, el equipo colaboró activamente en el repositorio oficial de la aplicación web ([Full_Tank_Frontend](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend)) para la implementación modular de los Bounded Contexts en Vue 3 y PrimeVue, la ejecución de pruebas unitarias con Vitest y el despliegue funcional en Firebase Hosting.

Evidencia de Colaboración:

Captura de pantalla de commits en GitHub mostrando contribuciones del equipo.

##### Insights
![Insights](../assets/chapter-5/insishts-2.png)

##### Contributors
![Contributors](../assets/chapter-5/contribuitors-2.png)

##### Network graph
![Network graph](../assets/chapter-5/network-2.png)

Principales Herramientas de Comunicación:
- GitHub (control de versiones, pull requests y code review cruzado)
- WhatsApp (coordinación técnica inmediata y sincronización diaria)
- Google Meet (reuniones de planificación y retrospectiva del sprint)

Se contrastó la planificación de responsabilidades con los Pull Requests integrados del frontend al **9 de octubre de 2026**. La consulta oficial registra la totalidad de diez Pull Requests de funcionalidades (#2 al #11) integrados satisfactoriamente hacia `develop` y posteriormente fusionados a `main`. Todos los integrantes del equipo cuentan con participación técnica y autoría comprobada de Pull Requests en el repositorio oficial:

| Contexto / Bounded Context | Autor(es) | Evidencia oficial | Estado |
|---|---|---|---|
| Shared Base & Coord. | Brayan Corvacho (`BralexCD`) | PR #2 (`feat/shared`) | Integrado en `develop` y `main`. |
| IAM & Session | Brayan Corvacho (`BralexCD`) | PR #3 (`feat/iam`) | Integrado en `develop` y `main`. |
| Fulfillment | Frank Huingo (`Franz2308`) | PR #4 (`feat/fulfillment`) | Integrado en `develop` y `main`. |
| Notification | Frank Huingo (`Franz2308`) | PR #5 (`feat/notification`) | Integrado en `develop` y `main`. |
| Equipment | Joan Carhuayal (`JoanCS`) | PR #6 (`feat/equipment`) | Integrado en `develop` y `main`. |
| Inventory | Joan Carhuayal (`JoanCS`) | PR #7 (`feat/inventory`) | Integrado en `develop` y `main`. |
| Catalog | Enrique Mantilla (`enrique-mantilla`) | PR #8 (`feat/catalog`) | Integrado en `develop` y `main`. |
| Ordering | Enrique Mantilla (`enrique-mantilla`) | PR #9 (`feat/ordering`) | Integrado en `develop` y `main`. |
| Payment | Joan Payano (`joanfpp2-ai`) | PR #10 (`feat/payment`) | Integrado en `develop` y `main`. |
| Reporting | Joan Payano (`joanfpp2-ai`) | PR #11 (`feat/reporting`) | Integrado en `develop` y `main`. |

Fuentes: [Pull Requests del frontend](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend/pulls), [Contributors](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend/graphs/contributors), [Network Graph](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend/network) y [consulta conservada de la API](../assets/chapter-5/ejecucion-tb1/github-pull-requests.json).

La integración exitosa de los diez Pull Requests demuestra el trabajo coordinado de los cinco integrantes del equipo bajo la estrategia GitFlow. Cada Bounded Context fue desarrollado en su rama temática correspondiente, validado con sus respectivas pruebas unitarias y coordinado a través del bus de eventos transversal (`coordination.service.js`) antes de su consolidación final y despliegue a producción.

##### Acciones de mejora y compromisos para Sprint 3 (AV2)

- Conectar el frontend SPA con la API RESTful de backend implementada en ASP.NET Core, sustituyendo los adaptadores en memoria.
- Diseñar la persistencia en base de datos relacional PostgreSQL/SQL Server asegurando integridad referencial en transacciones de combustible y pedidos.
- Extender la cobertura de pruebas hacia pruebas de integración end-to-end (E2E) con Playwright/Cypress.
- Ajustar el compromiso de historias de usuario a la velocidad histórica demostrada en este primer sprint (velocidad real observada).
- Incorporar pasarela de pago real y subida de comprobantes bancarios conforme a los criterios de aceptación de US-08.

Estos puntos consolidan las lecciones aprendidas durante la ejecución de TB1 y guiarán el desarrollo del Sprint 3 para la Entrega AV2.

---

### 5.2.3. Sprint 3

#### 5.2.3.1. Sprint Planning 3

El tercer sprint se orientó a la construcción de los **Web Services RESTful de FullTank** en C# con ASP.NET Core, su persistencia relacional mediante Entity Framework Core, la preparación del despliegue en la nube y la integración con la Web Application desarrollada en el Sprint 2.

<table border="1" cellpadding="6" cellspacing="0" style="border-collapse: collapse; width: 100%;">
    <tr align="center" style="background-color: #f2f2f2;">
        <td><strong>Sprint #</strong></td>
        <td><strong>Sprint 3</strong></td>
    </tr>
    <tr>
        <td colspan="2" align="center" style="background-color: #eaeaea;"><strong>Sprint Planning Background</strong></td>
    </tr>
    <tr align="center">
        <td><strong>Date</strong></td>
        <td>2026-10-20</td>
    </tr>
    <tr align="center">
        <td><strong>Time</strong></td>
        <td>04:00 PM</td>
    </tr>
    <tr align="center">
        <td><strong>Location</strong></td>
        <td>Google Meet (Sesión virtual de equipo)</td>
    </tr>
    <tr align="center">
        <td><strong>Prepared By</strong></td>
        <td>Corvacho Damian, Brayan Alexis</td>
    </tr>
    <tr align="center">
        <td><strong>Attendees (to planning meeting)</strong></td>
        <td>
          Corvacho Damian, Brayan Alexis — U20231A257<br>
          Huingo Tello, Frank Anthony — U202319057<br>
          Payano Puchuri, Joan Fabricio — U202318620<br>
          Mantilla Maldonado, Enrique Manuel — U20231B842
        </td>
    </tr>
    <tr align="center">
        <td><strong>Sprint 2 Review Summary</strong></td>
        <td>Se integraron los diez Pull Requests de la Web Application (#2 al #11) en <code>develop</code> y <code>main</code>, con 90/90 pruebas aprobadas en Vitest y despliegue automatizado en Firebase Hosting (release <code>v1.0.0</code>). La aplicación funcionaba con una API simulada en memoria, por lo que la persistencia real y los Web Services quedaron como objetivo del siguiente sprint. Quedaron pendientes la recuperación de contraseña (US-16) y la descarga de reportes en PDF (US-35).</td>
    </tr>
    <tr align="center">
        <td><strong>Sprint 2 Retrospective Summary</strong></td>
        <td>Se acordó sustituir los adaptadores en memoria por una API RESTful propia, mantener la misma división por Bounded Contexts en el backend y ajustar el compromiso a la capacidad actual del equipo de cuatro integrantes. Para la persistencia inicial se seleccionó MySQL 8 (posteriormente migrado a PostgreSQL 18 en Render Free) por su soporte en Entity Framework Core y despliegue en contenedor. El pago se mantiene como una simulación académica explícita sin pasarela bancaria real.</td>
    </tr>
    <tr>
        <td colspan="2" align="center" style="background-color: #eaeaea;"><strong>Sprint Goal &amp; User Stories</strong></td>
    </tr>
    <tr>
        <td align="center"><strong>Sprint 3 Goal</strong></td>
        <td>Our focus is on implementing and deploying the FullTank RESTful Web Services in ASP.NET Core with relational persistence across all nine Bounded Contexts (IAM, Catalog, Inventory, Ordering, Equipment, Fulfillment, Payment, Notification, and Reporting &amp; Analytics) and connecting them to the Web Application. We believe it delivers persistent end-to-end B2B fuel ordering, fleet dispatch, and simulated receipt issuance to fuel buyers and suppliers. This will be confirmed when the deployed frontend executes the complete catalog-to-receipt workflow against the cloud API with automated test coverage.</td>
    </tr>
    <tr align="center">
        <td><strong>Sprint 3 Velocity</strong></td>
        <td>64</td>
    </tr>
    <tr align="center">
        <td><strong>Sum of Story Points</strong></td>
        <td>64 *(27 historias técnicas, TS-01 a TS-27; duración: 3 semanas)*</td>
    </tr>
</table>

##### Historias planificadas en el Sprint 3

El Sprint 3 comprende las 27 historias técnicas de la API definidas en la sección [3.1.2](chapter3.md#312-historias-técnicas). Por indicación del docente, el orden de implementación priorizó las funcionalidades del MVP (catálogo, inventario, pedidos, logística y pagos) antes de IAM; por ello, la columna *Orden* no coincide con la posición de las historias en la tabla de la sección 3.3.

| Orden | ID | Título | Bounded Context | Story Points |
|:---:|:---:|---|---|:---:|
| 1 | TS-11 | Endpoint: Gestionar productos de combustible | Catalog / Inventory | 3 |
| 2 | TS-12 | Endpoint: Actualizar stock de producto | Inventory | 2 |
| 3 | TS-22 | Endpoint: Calificar proveedores | Catalog | 2 |
| 4 | TS-15 | Endpoint: Gestionar solicitudes de combustible | Ordering | 3 |
| 5 | TS-16 | Endpoint: Consultar solicitud por identificador | Ordering | 2 |
| 6 | TS-04 | Endpoint: Crear pedido | Ordering | 3 |
| 7 | TS-05 | Endpoint: Consultar pedidos por usuario | Ordering | 2 |
| 8 | TS-13 | Endpoint: Consultar pedidos | Ordering | 2 |
| 9 | TS-14 | Endpoint: Confirmar o cancelar pedido | Ordering | 2 |
| 10 | TS-23 | Endpoint: Gestionar equipos | Equipment | 3 |
| 11 | TS-24 | Endpoint: Asignar proveedor favorito | Equipment / Catalog | 2 |
| 12 | TS-25 | Endpoint: Eliminar equipo | Equipment | 1 |
| 13 | TS-17 | Endpoint: Gestionar entregas | Fulfillment | 3 |
| 14 | TS-18 | Endpoint: Gestionar conductores | Fulfillment | 3 |
| 15 | TS-19 | Endpoint: Gestionar vehículos | Fulfillment | 3 |
| 16 | TS-20 | Endpoint: Registrar y validar pagos | Payment | 3 |
| 17 | TS-21 | Endpoint: Consultar pagos | Payment | 2 |
| 18 | TS-26 | Endpoint: Gestionar notificaciones | Notification | 2 |
| 19 | TS-27 | Endpoint: Reportes y analítica | Reporting & Analytics | 3 |
| 20 | TS-08 | Endpoint: Gestionar empresas solicitantes | IAM | 3 |
| 21 | TS-09 | Endpoint: Gestionar empresas proveedoras | IAM | 3 |
| 22 | TS-01 | Endpoint: Login | IAM | 2 |
| 23 | TS-06 | Endpoint: Registrar usuario | IAM | 3 |
| 24 | TS-07 | Endpoint: Consultar usuarios | IAM | 2 |
| 25 | TS-10 | Endpoint: Actualizar perfil de usuario | IAM | 2 |
| 26 | TS-02 | Endpoint: Recuperar contraseña | IAM | 2 |
| 27 | TS-03 | Endpoint: Logout | IAM | 1 |
| **Total** | **27** | — | — | **64 SP** |

---

#### 5.2.3.2. Aspect Leaders and Collaborators

Para el Sprint 3 el equipo activo de cuatro integrantes distribuyó el liderazgo técnico (`L`) y la colaboración (`C`) sobre quince aspectos clave de la API RESTful y su integración en la nube: base compartida (`Shared Base`), los nueve Bounded Contexts de negocio (`IAM`, `Catalog`, `Inventory`, `Ordering`, `Equipment`, `Fulfillment`, `Notification`, `Payment`, `Reporting`), persistencia en Entity Framework Core (`Persistence`), configuración de hosting y salud (`Hosting & Config`), pruebas automatizadas en xUnit (`xUnit Tests`), contenedorización y despliegue en Render (`Docker & Render`) y documentación técnica (`Documentation`).

<table border="1" cellpadding="6" cellspacing="0" style="border-collapse: collapse; width: 100%;">
    <thead>
        <tr align="center" style="background-color: #f2f2f2;">
            <th>Team Member<br>(Last Name, First Name)</th>
            <th>GitHub Username</th>
            <th>Shared Base<br>(L/C)</th>
            <th>IAM<br>(L/C)</th>
            <th>Catalog<br>(L/C)</th>
            <th>Inventory<br>(L/C)</th>
            <th>Ordering<br>(L/C)</th>
            <th>Persistence<br>(L/C)</th>
            <th>Equipment<br>(L/C)</th>
            <th>Fulfillment<br>(L/C)</th>
            <th>Notification<br>(L/C)</th>
            <th>Payment<br>(L/C)</th>
            <th>Reporting<br>(L/C)</th>
            <th>Hosting &amp; Config<br>(L/C)</th>
            <th>xUnit Tests<br>(L/C)</th>
            <th>Docker &amp; Render<br>(L/C)</th>
            <th>Documentation<br>(L/C)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Corvacho Damian, Brayan Alexis</td>
            <td>BralexCD</td>
            <td align="center"><strong>L</strong></td>
            <td align="center"><strong>L</strong></td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center"><strong>L</strong></td>
            <td align="center"><strong>L</strong></td>
            <td align="center">C</td>
            <td align="center"><strong>L</strong></td>
        </tr>
        <tr>
            <td>Mantilla Maldonado, Enrique Manuel</td>
            <td>enrique-mantilla</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center"><strong>L</strong></td>
            <td align="center"><strong>L</strong></td>
            <td align="center"><strong>L</strong></td>
            <td align="center"><strong>L</strong></td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center"><strong>L</strong></td>
            <td align="center">C</td>
        </tr>
        <tr>
            <td>Huingo Tello, Frank Anthony</td>
            <td>Franz2308</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center"><strong>L</strong></td>
            <td align="center"><strong>L</strong></td>
            <td align="center"><strong>L</strong></td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center"><strong>L</strong></td>
            <td align="center"><strong>L</strong></td>
        </tr>
        <tr>
            <td>Payano Puchuri, Joan Fabricio</td>
            <td>joanfpp2-ai</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center"><strong>L</strong></td>
            <td align="center"><strong>L</strong></td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
            <td align="center">C</td>
        </tr>
    </tbody>
</table>

*Nota de coliderazgo técnico:* En *Pruebas automatizadas (xUnit)* cada integrante desarrolló su propia suite de pruebas (dominio, IAM, órdenes y checkout) con revisión cruzada; en *Docker & Render*, Frank Huingo lideró la definición del contenedor Docker y Enrique Mantilla la configuración inicial del Blueprint de Render, mientras que Brayan Corvacho ejecutó la migración final a PostgreSQL 18 y despliegue en Render Free; y en *Documentación*, Frank Huingo y Brayan Corvacho co-lideraron la actualización del Sprint 3.

---

#### 5.2.3.3. Sprint Backlog 3

El objetivo principal del Sprint 3 es construir, probar y desplegar en la nube los Web Services RESTful de FullTank en ASP.NET Core con persistencia relacional y conectar la Web Application en producción para soportar el ciclo operativo completo entre compradores y proveedores.

**Tablero del Sprint Backlog:** [FullTank · FuelPoint | Sprint 3 en Trello](https://trello.com/b/CBQSmZA1/sprint-3).

<div align="center">
  <img src="../assets/chapter-5/trello-sprint-3.png" alt="Tablero de Trello oficial de FullTank para el Sprint 3 con las 27 historias técnicas" width="850"/>
  <p><em>Figura: Tablero de Trello oficial de FullTank para el Sprint 3, mostrando el flujo y la categorización de las 27 historias técnicas de la API RESTful.</em></p>
</div>

Los estados de la tabla se determinaron contrastando el código integrado en `main` (commit `daee12a`) con los criterios de cada historia técnica y con las evidencias de despliegue en producción. Conforme al formato del curso, los estados se normalizan en `Done` (implementado y verificado mediante pruebas o despliegue), `In-Process` (implementación parcial pendiente de completar alguna operación o reconciliación de contrato) y `To-do` (pendiente de implementación para el Sprint 4).

<table border="1" cellpadding="6" cellspacing="0" style="border-collapse: collapse; width: 100%;">
    <tr align="center" style="background-color: #f2f2f2;">
        <td colspan="2"><strong>Sprint #</strong></td>
        <td colspan="6"><strong>Sprint 3</strong></td>
    </tr>
    <tr align="center" style="background-color: #eaeaea;">
        <td colspan="2"><strong>User Story</strong></td>
        <td colspan="6"><strong>Work-Item / Task</strong></td>
    </tr>
    <tr align="center" style="background-color: #f9f9f9;">
        <td><strong>Story Id</strong></td>
        <td><strong>Story Title</strong></td>
        <td><strong>Task Id</strong></td>
        <td><strong>Task Title</strong></td>
        <td><strong>Task Description</strong></td>
        <td><strong>Estimation (Hours)</strong></td>
        <td><strong>Assigned To</strong></td>
        <td><strong>Status (To-do / In-Process / To-Review / Done)</strong></td>
    </tr>
    <tr>
        <td align="center">Technical Support</td>
        <td>Arquitectura base y contratos compartidos</td>
        <td align="center">TSK-301</td>
        <td>Configuración de solución .NET y Shared</td>
        <td>Configurar la solución .NET 10, contratos de dominio compartidos, despacho de eventos de dominio y manejo localizado de errores.</td>
        <td align="center">6</td>
        <td>Brayan Corvacho</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">TS-08, TS-09</td>
        <td>Endpoint: Gestionar empresas solicitantes y proveedoras</td>
        <td align="center">TSK-302</td>
        <td>Modelo de empresas y propietarios</td>
        <td>Modelar e implementar entidades, repositorios y servicios para empresas compradoras, proveedoras y propietarios de cuenta.</td>
        <td align="center">5</td>
        <td>Brayan Corvacho</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">TS-11, TS-22</td>
        <td>Endpoint: Gestionar productos / Calificar proveedores</td>
        <td align="center">TSK-303</td>
        <td>Implementación de Catalog</td>
        <td>Implementar productos de combustible, proveedores favoritos, calificaciones y sus controladores REST.</td>
        <td align="center">6</td>
        <td>Enrique Mantilla</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">TS-11, TS-12</td>
        <td>Endpoint: Gestionar productos / Actualizar stock</td>
        <td align="center">TSK-304</td>
        <td>Implementación de Inventory</td>
        <td>Implementar control de stock con concurrencia, reservas de inventario y registro de movimientos IN/OUT.</td>
        <td align="center">7</td>
        <td>Enrique Mantilla</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">TS-05, TS-13, TS-14, TS-16</td>
        <td>Endpoints de consulta y ciclo de vida de pedidos</td>
        <td align="center">TSK-305</td>
        <td>Implementación de Ordering</td>
        <td>Implementar solicitudes de combustible, órdenes y transiciones aprobar → despachar → recibir → pagar, además de cancelación.</td>
        <td align="center">8</td>
        <td>Enrique Mantilla</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">TS-04, TS-15</td>
        <td>Endpoint: Crear pedido / Gestionar solicitudes</td>
        <td align="center">TSK-306</td>
        <td>Reconciliación de creación y rechazo</td>
        <td>Reconciliar la creación de pedidos (<code>POST /orders</code> deshabilitado; la orden nace al aprobar solicitud) y el rechazo de solicitudes con TS-04 y TS-15.</td>
        <td align="center">4</td>
        <td>Enrique Mantilla</td>
        <td align="center">In-Process</td>
    </tr>
    <tr>
        <td align="center">TS-23</td>
        <td>Endpoint: Gestionar equipos</td>
        <td align="center">TSK-307</td>
        <td>Implementación de Equipment</td>
        <td>Implementar gestión de equipos del comprador, niveles de combustible e historial de recargas.</td>
        <td align="center">6</td>
        <td>Frank Huingo</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">TS-24</td>
        <td>Endpoint: Asignar proveedor favorito</td>
        <td align="center">TSK-308</td>
        <td>Proveedor favorito por equipo</td>
        <td>Verificar y completar la vinculación de proveedor favorito directamente a un equipo específico del comprador.</td>
        <td align="center">4</td>
        <td>Por asignar</td>
        <td align="center">In-Process</td>
    </tr>
    <tr>
        <td align="center">TS-17, TS-18, TS-19</td>
        <td>Endpoints de entregas, conductores y vehículos</td>
        <td align="center">TSK-309</td>
        <td>Implementación de Fulfillment</td>
        <td>Implementar gestión de conductores, vehículos cisterna, disponibilidad de flota y registro de entregas.</td>
        <td align="center">8</td>
        <td>Frank Huingo</td>
        <td align="center">In-Process</td>
    </tr>
    <tr>
        <td align="center">TS-26</td>
        <td>Endpoint: Gestionar notificaciones</td>
        <td align="center">TSK-310</td>
        <td>Implementación de Notification</td>
        <td>Implementar generación de alertas ante cambios de estado de órdenes y marcado de lectura individual y masivo.</td>
        <td align="center">5</td>
        <td>Frank Huingo</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">TS-20, TS-21</td>
        <td>Endpoint: Registrar, validar y consultar pagos</td>
        <td align="center">TSK-311</td>
        <td>Implementación de Payment (simulado)</td>
        <td>Implementar checkout simulado atómico con cálculo de IGV (18 %), registro de pagos y emisión de comprobantes académicos <code>SIM-INV-*</code>.</td>
        <td align="center">7</td>
        <td>Joan Payano</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">TS-27</td>
        <td>Endpoint: Reportes y analítica</td>
        <td align="center">TSK-312</td>
        <td>Implementación de Reporting &amp; Analytics</td>
        <td>Implementar endpoints de indicadores de gasto del comprador y ventas del proveedor para los dashboards.</td>
        <td align="center">7</td>
        <td>Joan Payano</td>
        <td align="center">In-Process</td>
    </tr>
    <tr>
        <td align="center">TS-01, TS-06, TS-07, TS-10</td>
        <td>Endpoints de login, registro, usuarios y perfil</td>
        <td align="center">TSK-313</td>
        <td>Implementación de IAM</td>
        <td>Implementar hashing BCrypt, emisión de JWT, registro con <code>registrationToken</code>, sign-in, sign-up y actualización de perfil.</td>
        <td align="center">8</td>
        <td>Brayan Corvacho</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">Technical Support</td>
        <td>Persistencia relacional y migraciones</td>
        <td align="center">TSK-314</td>
        <td>Contexto EF Core y migraciones</td>
        <td>Configurar <code>AppDbContext</code>, Unit of Work y migraciones iniciales de Entity Framework Core.</td>
        <td align="center">5</td>
        <td>Enrique Mantilla</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">Technical Support</td>
        <td>Salud del servicio y datos semilla</td>
        <td align="center">TSK-315</td>
        <td>Configuración de hosting y seeder</td>
        <td>Validar configuración segura de producción, endpoint <code>/health</code>, registro modular y carga inicial de datos demo.</td>
        <td align="center">5</td>
        <td>Brayan Corvacho</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">Technical Support</td>
        <td>Calidad de dominio</td>
        <td align="center">TSK-316</td>
        <td>Pruebas xUnit de reglas de dominio</td>
        <td>Escribir pruebas unitarias de invariantes de dominio y conversión de unidades de combustible.</td>
        <td align="center">4</td>
        <td>Frank Huingo</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">TS-06</td>
        <td>Endpoint: Registrar usuario</td>
        <td align="center">TSK-317</td>
        <td>Pruebas xUnit de registro IAM</td>
        <td>Escribir pruebas unitarias para flujo de registro con token corporativo y validación de propiedad de empresas.</td>
        <td align="center">4</td>
        <td>Brayan Corvacho</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">TS-14, TS-15</td>
        <td>Endpoints de pedidos y solicitudes</td>
        <td align="center">TSK-318</td>
        <td>Pruebas xUnit del flujo de órdenes</td>
        <td>Escribir pruebas automatizadas de aprobación de solicitudes, despacho de flota y confirmación de recepción.</td>
        <td align="center">5</td>
        <td>Enrique Mantilla</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">TS-20</td>
        <td>Endpoint: Registrar y validar pagos</td>
        <td align="center">TSK-319</td>
        <td>Pruebas xUnit de checkout y recibos</td>
        <td>Escribir pruebas automatizadas sobre cálculo de totales, IGV y emisión de comprobantes de pago simulado.</td>
        <td align="center">4</td>
        <td>Joan Payano</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">Technical Support</td>
        <td>Seguridad multiempresa y configuración</td>
        <td align="center">TSK-320</td>
        <td>Pruebas xUnit de seguridad y config</td>
        <td>Escribir pruebas de aislamiento de acceso entre empresas y rechazo de configuraciones inseguras en producción.</td>
        <td align="center">5</td>
        <td>Brayan Corvacho</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">Technical Support</td>
        <td>Empaquetado en contenedores</td>
        <td align="center">TSK-321</td>
        <td>Imagen Docker de la API .NET</td>
        <td>Definir <code>Dockerfile</code> multietapa de la API RESTful y validar construcción de imagen Release.</td>
        <td align="center">4</td>
        <td>Frank Huingo</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">Technical Support</td>
        <td>Infraestructura como código en nube</td>
        <td align="center">TSK-322</td>
        <td>Blueprint de Render y BD privada</td>
        <td>Configurar Blueprint <code>render.yaml</code> para orquestar la API en contenedor y base de datos privada en Render.</td>
        <td align="center">5</td>
        <td>Enrique Mantilla</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">TS-02</td>
        <td>Endpoint: Recuperar contraseña</td>
        <td align="center">TSK-323</td>
        <td>Recuperación de contraseña</td>
        <td>Implementar endpoint y flujo de restablecimiento de contraseña por correo electrónico (planificado para Sprint 4).</td>
        <td align="center">5</td>
        <td>Por asignar</td>
        <td align="center">To-do</td>
    </tr>
    <tr>
        <td align="center">TS-03</td>
        <td>Endpoint: Logout</td>
        <td align="center">TSK-324</td>
        <td>Cierre de sesión en backend JWT</td>
        <td>Definir e implementar revocación/cierre de sesión en el backend JWT (planificado para Sprint 4).</td>
        <td align="center">3</td>
        <td>Por asignar</td>
        <td align="center">To-do</td>
    </tr>
    <tr>
        <td align="center">TS-25</td>
        <td>Endpoint: Eliminar equipo</td>
        <td align="center">TSK-325</td>
        <td>Eliminación segura de equipos</td>
        <td>Implementar endpoint <code>DELETE</code> de equipos validando ausencia de pedidos en curso.</td>
        <td align="center">4</td>
        <td>Por asignar</td>
        <td align="center">To-do</td>
    </tr>
    <tr>
        <td align="center">TS-17, TS-18, TS-19</td>
        <td>Endpoints de entregas, conductores y vehículos</td>
        <td align="center">TSK-326</td>
        <td>Baja de flota y entrega fallida</td>
        <td>Implementar <code>DELETE</code> de conductores y vehículos y registro de incidencia por entrega fallida.</td>
        <td align="center">6</td>
        <td>Por asignar</td>
        <td align="center">To-do</td>
    </tr>
    <tr>
        <td align="center">TS-27</td>
        <td>Endpoint: Reportes y analítica</td>
        <td align="center">TSK-327</td>
        <td>Exportación de reportes en PDF</td>
        <td>Implementar generación y exportación de reportes analíticos de consumo y ventas en formato PDF.</td>
        <td align="center">6</td>
        <td>Por asignar</td>
        <td align="center">To-do</td>
    </tr>
    <tr>
        <td align="center">Technical Support</td>
        <td>Despliegue productivo en Render</td>
        <td align="center">TSK-328</td>
        <td>Despliegue PostgreSQL 18 y verificación</td>
        <td>Aplicar Blueprint en Render con PostgreSQL 18 y verificar <code>/health</code> y Swagger UI públicos en producción.</td>
        <td align="center">5</td>
        <td>Brayan Corvacho</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">Technical Support</td>
        <td>Integración Frontend–Backend</td>
        <td align="center">TSK-329</td>
        <td>Conexión de Web App con API pública</td>
        <td>Conectar el frontend en Firebase Hosting con la API pública en Render y validar el flujo integrado.</td>
        <td align="center">5</td>
        <td>Brayan Corvacho</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td align="center">Technical Support</td>
        <td>Documentación del Sprint 3</td>
        <td align="center">TSK-330</td>
        <td>Documentación del informe AV2</td>
        <td>Documentar planificación, arquitectura, evidencias de ejecución, despliegue y validación del Sprint 3.</td>
        <td align="center">6</td>
        <td>Frank Huingo, Brayan Corvacho</td>
        <td align="center">Done</td>
    </tr>
    <tr>
        <td colspan="5" align="right"><strong>Total Estimated Hours (Sprint 3)</strong></td>
        <td align="center"><strong>162</strong></td>
        <td colspan="2"></td>
    </tr>
</table>

**Resumen de avance de las historias técnicas:** 17 historias en *Done* (40 SP), 7 en *In-Process* (20 SP: TS-04, TS-15, TS-17, TS-18, TS-19, TS-24 y TS-27) y 3 en *To-do* (4 SP: TS-02, TS-03 y TS-25), sobre 64 SP planificados. En TSK-311, el estado *Done* corresponde al alcance académico de checkout simulado definido en 5.2.3.1.

**Coherencia del flujo de pagos:** el flujo implementado es *aprobar solicitud → despachar → confirmar recepción → pagar (checkout simulado) → comprobante*. La aprobación del proveedor reserva stock sin requerir un depósito previo, y el pago no procesa dinero, garantizando una transacción atómica y consistente.

---

#### 5.2.3.4. Development Evidence for Sprint Review

**Repositorios oficiales del Sprint 3:** [Full_Tank_Backend](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend) y [Full_Tank_Frontend](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend) (integración con la API en producción).

El historial de `main` del backend se verificó sobre el repositorio integrado el **12 de noviembre de 2026**, apuntando al commit de release [`daee12a`](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend/commit/daee12a) (*Merge branch 'release/postgresql' into main*), con **98 commits** (73 commits de trabajo y 25 merges `--no-ff`). Las ramas funcionales se consolidaron inicialmente mediante `release/backend` (`fde0498`, MySQL 8) y luego se migraron a **PostgreSQL 18** en Render Free mediante `release/postgresql` (`daee12a`), conectando finalmente el frontend en Firebase Hosting (`503ecd5`).

<table border="1" cellpadding="6" cellspacing="0" style="border-collapse: collapse; width: 100%;">
    <thead>
        <tr align="center" style="background-color: #f2f2f2;">
            <th>Repository</th>
            <th>Branch</th>
            <th>Commit Id</th>
            <th>Commit Message</th>
            <th>Commit Message Body</th>
            <th>Commited on (Date)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>chore/project-setup</td>
            <td>97f61a1</td>
            <td>chore: set up the .NET solution and project settings</td>
            <td>Creación de la solución .NET y configuración base de proyectos.</td>
            <td>2026-10-12</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>chore/project-setup</td>
            <td>a4e85c0</td>
            <td>feat(shared): define domain contracts and fuel units</td>
            <td>Definición de contratos base de dominio y unidades de combustible.</td>
            <td>2026-10-12</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>chore/project-setup</td>
            <td>556c036</td>
            <td>feat(shared): dispatch domain events</td>
            <td>Implementación del despachador interno de eventos de dominio.</td>
            <td>2026-10-12</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>chore/project-setup</td>
            <td>bfd1454</td>
            <td>feat(api): localize errors and handle exceptions</td>
            <td>Manejo centralizado de excepciones y errores localizados en la API.</td>
            <td>2026-10-12</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>chore/project-setup</td>
            <td>163efdd</td>
            <td>feat(companies): model buyers, suppliers and account owners</td>
            <td>Modelado de empresas compradoras, proveedoras y propietarios de cuenta.</td>
            <td>2026-10-13</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>chore/project-setup</td>
            <td>57375e2</td>
            <td>feat(shared): define contracts between modules</td>
            <td>Contratos de integración ACL entre los Bounded Contexts del sistema.</td>
            <td>2026-10-13</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>feat/catalog</td>
            <td>74c3ab8</td>
            <td>feat(catalog): model fuel products, favorites and ratings</td>
            <td>Entidades de productos de combustible, proveedores favoritos y calificaciones.</td>
            <td>2026-10-13</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>feat/catalog</td>
            <td>00a79a3</td>
            <td>feat(catalog): expose products, favorites and ratings</td>
            <td>Controladores y endpoints RESTful del módulo Catalog.</td>
            <td>2026-10-22</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>feat/inventory</td>
            <td>5deb465</td>
            <td>feat(inventory): model stock levels and fuel movements</td>
            <td>Modelo de niveles de inventario y movimientos de entrada/salida.</td>
            <td>2026-10-13</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>feat/inventory</td>
            <td>ba94c15</td>
            <td>feat(inventory): expose stock and movement endpoints</td>
            <td>Endpoints RESTful de gestión de stock, reservas y movimientos.</td>
            <td>2026-10-22</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>feat/equipment</td>
            <td>9f60900</td>
            <td>feat(equipment): model equipment and refill history</td>
            <td>Entidades de equipos del comprador e historial de recargas.</td>
            <td>2026-10-15</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>feat/equipment</td>
            <td>527a288</td>
            <td>feat(equipment): expose equipment and refill endpoints</td>
            <td>Endpoints RESTful para consulta, alta y edición de equipos.</td>
            <td>2026-10-22</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>feat/orders</td>
            <td>00ce34f</td>
            <td>feat(orders): define requests, orders and lifecycle rules</td>
            <td>Entidades de solicitudes y órdenes con reglas de transición de estado.</td>
            <td>2026-10-15</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>feat/orders</td>
            <td>0be20bc</td>
            <td>feat(orders): expose approval, dispatch and receipt actions</td>
            <td>Endpoints RESTful de aprobación, despacho, recepción y cancelación.</td>
            <td>2026-10-23</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>feat/fulfillment</td>
            <td>19223f5</td>
            <td>feat(fulfillment): model drivers, vehicles and deliveries</td>
            <td>Modelo de conductores, cisternas y registro logístico de entregas.</td>
            <td>2026-10-16</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>feat/fulfillment</td>
            <td>349a01b</td>
            <td>feat(fulfillment): expose fleet availability and deliveries</td>
            <td>Endpoints RESTful de disponibilidad de flota y control de entregas.</td>
            <td>2026-10-23</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>feat/payments</td>
            <td>b1e8f3c</td>
            <td>feat(payment): model payments and academic receipts</td>
            <td>Modelo de pagos y comprobantes académicos del flujo de facturación.</td>
            <td>2026-10-19</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>feat/payments</td>
            <td>5b21a43</td>
            <td>feat(payment): expose checkout and payment history</td>
            <td>Endpoints RESTful de checkout simulado atómico e historial de pagos.</td>
            <td>2026-10-26</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>feat/notifications</td>
            <td>7523521</td>
            <td>feat(notification): model alerts and read status</td>
            <td>Modelo de notificaciones operativas y control de lectura.</td>
            <td>2026-10-26</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>feat/notifications</td>
            <td>de3b052</td>
            <td>feat(notification): expose alerts and mark them as read</td>
            <td>Endpoints RESTful de consulta y marcado individual/masivo de alertas.</td>
            <td>2026-10-27</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>feat/analytics</td>
            <td>8735ec5</td>
            <td>feat(analytics): define spending and sales summaries</td>
            <td>Contratos y cálculos de resúmenes de gasto y ventas por período.</td>
            <td>2026-10-26</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>feat/analytics</td>
            <td>f7f4e52</td>
            <td>feat(analytics): expose buyer and supplier dashboards</td>
            <td>Endpoints RESTful analíticos para dashboards de comprador y proveedor.</td>
            <td>2026-10-28</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>feat/accounts</td>
            <td>b040146</td>
            <td>feat(iam): secure account access with BCrypt and JWT</td>
            <td>Autenticación con hashing BCrypt y generación de tokens JWT.</td>
            <td>2026-11-02</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>feat/accounts</td>
            <td>01696ec</td>
            <td>feat(iam): expose sign-in, sign-up and profile endpoints</td>
            <td>Endpoints RESTful de autenticación, registro con token y perfiles.</td>
            <td>2026-11-02</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>feat/database</td>
            <td>28dc91a</td>
            <td>feat(database): wire the context and unit of work</td>
            <td>Configuración de <code>AppDbContext</code> y patrón Unit of Work.</td>
            <td>2026-11-03</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>feat/database</td>
            <td>c6acfaf</td>
            <td>feat(database): track the MySQL schema with EF migrations</td>
            <td>Generación de migraciones de esquema relacional en EF Core.</td>
            <td>2026-11-03</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>feat/app-setup</td>
            <td>a551f0f</td>
            <td>feat(hosting): validate production settings and check MySQL</td>
            <td>Validación estricta de configuración en producción y health check de BD.</td>
            <td>2026-11-03</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>feat/app-setup</td>
            <td>4a0ab19</td>
            <td>feat(platform): wire modules and load demo data</td>
            <td>Registro de módulos de dominio y carga idempotente de datos demo.</td>
            <td>2026-11-04</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>test/domain-rules</td>
            <td>ed2ba5e</td>
            <td>test(domain): check fuel units and entity invariants</td>
            <td>Suite xUnit de invariantes de entidades y conversión de unidades.</td>
            <td>2026-11-04</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>test/registration</td>
            <td>61c128c</td>
            <td>test(iam): verify registration and company ownership</td>
            <td>Pruebas xUnit de registro corporativo y validación de propiedad.</td>
            <td>2026-11-05</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>test/order-workflow</td>
            <td>ffc5804</td>
            <td>test(orders): cover approval, dispatch and receipt</td>
            <td>Pruebas xUnit del flujo completo aprobar → despachar → recibir.</td>
            <td>2026-11-05</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>test/payment-checkout</td>
            <td>4eef681</td>
            <td>test(payment): verify checkout totals and receipt data</td>
            <td>Pruebas xUnit de totales, IGV y comprobante académico del checkout.</td>
            <td>2026-11-05</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>test/registration</td>
            <td>ff11306</td>
            <td>test(security): reject access across company boundaries</td>
            <td>Pruebas xUnit de aislamiento y denegación de acceso entre empresas.</td>
            <td>2026-11-05</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>build/docker</td>
            <td>b32aa3e</td>
            <td>build: publish the API in a .NET Docker image</td>
            <td>Construcción de imagen Docker multietapa para ASP.NET Core 10.</td>
            <td>2026-11-06</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>chore/render</td>
            <td>b526de2</td>
            <td>chore(render): connect the API to private MySQL</td>
            <td>Definición del Blueprint <code>render.yaml</code> para despliegue en Render.</td>
            <td>2026-11-06</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>test/configuration</td>
            <td>277b258</td>
            <td>test(config): reject unsafe production settings</td>
            <td>Pruebas xUnit para bloquear credenciales inseguras en entorno Production.</td>
            <td>2026-11-06</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>docs/backend</td>
            <td>d3d0a98</td>
            <td>docs: explain backend setup and local run commands</td>
            <td>Documentación de ejecución local, variables de entorno y migraciones.</td>
            <td>2026-11-12</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>test/container</td>
            <td>19b00e7</td>
            <td>test(docker): check payment persistence after restart</td>
            <td>Prueba de humo en contenedores validando persistencia tras reinicio.</td>
            <td>2026-11-12</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>docs/backend</td>
            <td>d7f6c08</td>
            <td>docs(render): document deployment and verification steps</td>
            <td>Guía de despliegue y verificación pública en Render.</td>
            <td>2026-11-12</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>chore/db-tools</td>
            <td>2908b99</td>
            <td>chore(db-tools): register MCP tools and document their use</td>
            <td>Registro del servidor MCP para inspección de esquema y datos.</td>
            <td>2026-11-12</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>feat/postgresql</td>
            <td>5ddbe00</td>
            <td>feat(persistence): migrate the API schema to PostgreSQL</td>
            <td>Migración del esquema EF Core a PostgreSQL 18 para Render Free tier.</td>
            <td>2026-11-12</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend</td>
            <td>feat/postgresql</td>
            <td>cbde399</td>
            <td>ci(render): validate the PostgreSQL free stack</td>
            <td>Validación CI del stack completo con PostgreSQL en Render Free.</td>
            <td>2026-11-12</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend</td>
            <td>feat/backend-integration</td>
            <td>e9c9dab</td>
            <td>fix(api): align frontend flows with the real backend</td>
            <td>Alineamiento de adaptadores y flujos SPA del frontend con la API real.</td>
            <td>2026-11-12</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend</td>
            <td>feat/backend-integration</td>
            <td>aae3b91</td>
            <td>ci(firebase): publish the real API build from main</td>
            <td>Configuración de build productivo apuntando a la API desplegada en Render.</td>
            <td>2026-11-12</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend</td>
            <td>fix/e2e-polish</td>
            <td>5dd35ef</td>
            <td>fix(e2e): guard buyer fleet calls, label vehicle select, and fix invoice local date</td>
            <td>Correcciones de integración extremo a extremo y formato de fecha en facturas.</td>
            <td>2026-11-13</td>
        </tr>
        <tr>
            <td>1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend</td>
            <td>main</td>
            <td>503ecd5</td>
            <td>Merge branch 'develop' into main for Firebase deploy</td>
            <td>Publicación en Firebase Hosting de la versión integrada con la API real.</td>
            <td>2026-11-13</td>
        </tr>
    </tbody>
</table>

**Observación de proceso:** la política de 5.1.2 exige integrar mediante Pull Request con revisión por pares. En el backend la integración se hizo con merges locales (`--no-ff`), por lo que no existe evidencia de revisión mediante Pull Requests en GitHub. Se registra como acción de mejora para el Sprint 4 (ver 5.2.3.8).

---

#### 5.2.3.5. Execution Evidence for Sprint Review

La API se ejecutó y validó en un entorno local de contenedores el **7 de noviembre de 2026**. Esta validación comprueba la imagen de la API y su comunicación privada con MySQL; **no acredita el despliegue público en Render**, cuyas evidencias se registran en 5.2.3.7.

| Comprobación | Resultado |
|---|---|
| `dotnet test full-tank-platform.sln` | **82/82 pruebas aprobadas**, sin fallos |
| Construcción de la imagen de la API (`Dockerfile`, Release .NET 10) | Correcta |
| Construcción de la imagen de MySQL (`deploy/mysql/Dockerfile`, MySQL 8.0.46) | Correcta |
| Validación de `render.yaml` contra el esquema público de Render | Válido |
| Prueba de humo en contenedores (`deploy/smoke_render.py`) | **Aprobada** |

La prueba de humo crea una red, un volumen, MySQL y la API desechables, con contraseñas aleatorias, `ASPNETCORE_ENVIRONMENT=Production` y un límite de 512 MB por contenedor, y verifica:

1. La API escucha en todas las interfaces con un puerto distinto del predeterminado.
2. El proceso está activo, pero `/health` responde HTTP 503 mientras faltan las migraciones.
3. Las migraciones y los datos demo se aplican sobre una base vacía y `/health` pasa a HTTP 200.
4. Swagger es accesible e identifica el alcance simulado de los pagos.
5. CORS admite los orígenes de Firebase y rechaza un origen distinto.
6. El JWT es obligatorio para consultar órdenes; se inicia sesión con la cuenta compradora y con la proveedora.
7. El checkout académico genera un comprobante `SIM-INV-*`.
8. Tras reiniciar MySQL y la API, el pago se conserva y los datos demo no se duplican.

**Recorrido funcional evidenciado:** catálogo → solicitud del comprador → aprobación del proveedor → asignación de vehículo y conductor → despacho → confirmación de recepción → pago simulado → comprobante.

---

#### 5.2.3.6. Services Documentation Evidence for Sprint Review

La API expone documentación interactiva OpenAPI 3.0 mediante Swagger UI (título *FullTank API*, versión `v1`), disponible y operativa públicamente en la nube en `https://fulltank-av2-api-hqhk.onrender.com/swagger/index.html` (así como en el entorno local en `http://localhost:5204/swagger`). Los endpoints protegidos requieren el encabezado `Authorization: Bearer <token>` obtenido tras autenticarse mediante `/api/v1/authentication/sign-in`.

A continuación, se presentan las evidencias visuales de la interfaz Swagger UI en producción, organizada según los Bounded Contexts de la arquitectura del sistema:

<div align="center">
  <img src="../assets/chapter-5/despliegue/swagger-overview-analytics.png" alt="Documentación Swagger UI en Render - Visión general y Bounded Context Analytics (Reporting)" width="850"/>
  <p><em>Figura 5.2.3.6.1: Documentación Swagger UI en producción (Render) — Cabecera FullTank API v1 (OAS 3.0), autenticación JWT Bearer y endpoints analíticos de gastos y ventas (Reporting).</em></p>
</div>

<div align="center">
  <img src="../assets/chapter-5/despliegue/swagger-iam-fulfillment.png" alt="Documentación Swagger UI en Render - Bounded Contexts IAM (BuyerCompanies) y Fulfillment (Deliveries y Drivers)" width="850"/>
  <p><em>Figura 5.2.3.6.2: Documentación Swagger UI en producción — Endpoints de empresas compradoras (IAM) y gestión logística de despachos, entregas y conductores (Fulfillment).</em></p>
</div>

<div align="center">
  <img src="../assets/chapter-5/despliegue/swagger-equipment-catalog-inventory.png" alt="Documentación Swagger UI en Render - Bounded Contexts Equipment, Catalog (FavoriteProviders) e Inventory" width="850"/>
  <p><em>Figura 5.2.3.6.3: Documentación Swagger UI en producción — Endpoints de equipos industriales (Equipment), proveedores favoritos (Catalog) y existencias y movimientos de combustible (Inventory).</em></p>
</div>

<div align="center">
  <img src="../assets/chapter-5/despliegue/swagger-notifications-orders.png" alt="Documentación Swagger UI en Render - Bounded Contexts Notifications y Orders" width="850"/>
  <p><em>Figura 5.2.3.6.4: Documentación Swagger UI en producción — Endpoints de notificaciones y ciclo de vida de órdenes (Ordering), con protección del dominio ante creación directa.</em></p>
</div>

Las rutas siguientes corresponden a los endpoints RESTful implementados y operativos en la API; todas son relativas a `/api/v1` y utilizan la convención *kebab-case*:

| Contexto | Método | Ruta | Rol | Operación |
|---|---|---|---|---|
| IAM | POST | `/authentication/sign-in` | Público | Inicio de sesión: `{ email, password }` → `{ id, name, email, username, role, companyId, token }`. |
| IAM | POST | `/authentication/sign-up` | Público | Registro: `{ name, email, password, role, companyId, username, registrationToken }`. |
| IAM | GET / POST / PUT | `/buyer-companies`, `/buyer-companies/{id}` | Público (POST) / BUYER, PROVIDER | Registro, consulta y actualización de empresas compradoras; el POST devuelve el `registrationToken` (vigencia de 24 horas). |
| IAM | GET / POST / PUT | `/provider-companies`, `/provider-companies/{id}` | Público (POST) / BUYER, PROVIDER | Registro, consulta y actualización de empresas proveedoras. |
| IAM | GET / PUT | `/users/{id}`, `/users/{id}/profile`, `/users/{id}/password` | Usuario autenticado | Consulta del usuario, actualización del perfil propio y cambio de contraseña. |
| Catalog | GET / POST / PUT / DELETE | `/provider-products`, `/provider-products/{id}` | BUYER, PROVIDER (escritura: PROVIDER) | Productos de combustible del proveedor. |
| Catalog | GET / POST / DELETE | `/favorite-providers`, `/favorite-providers/{id}` | BUYER | Proveedores favoritos del comprador. |
| Catalog | GET / POST / PUT | `/provider-ratings`, `/provider-ratings/{id}` | BUYER | Calificaciones de proveedores. |
| Inventory | GET / POST / PUT / DELETE | `/inventory-items`, `/inventory-items/{id}` | BUYER, PROVIDER (escritura: PROVIDER) | Existencias, reservas y precios. |
| Inventory | GET / POST | `/inventory-movements`, `/inventory-movements/{id}` | PROVIDER | Movimientos de stock `IN`/`OUT`. |
| Ordering | GET / POST / PUT / DELETE | `/fuel-requests`, `/fuel-requests/{id}` | BUYER, PROVIDER (creación: BUYER) | Solicitudes de combustible. |
| Ordering | POST | `/fuel-requests/{id}/approve` | PROVIDER | Aprueba la solicitud, toma el precio del inventario, reserva stock y crea la orden en `ACCEPTED`. |
| Ordering | GET | `/orders`, `/orders/{id}` | BUYER, PROVIDER | Órdenes de la empresa autenticada. |
| Ordering | POST | `/orders/{id}/dispatch` | PROVIDER | `{ driverId, vehicleId }`; descuenta el stock reservado y pasa a `DISPATCHED`. |
| Ordering | POST | `/orders/{id}/receive` | BUYER | Confirma la recepción, libera conductor y vehículo, recarga el equipo y pasa a `PENDING_PAYMENT`. |
| Ordering | POST | `/orders/{id}/cancel` | PROVIDER | Cancela una orden `ACCEPTED` no despachada y libera el stock reservado. |
| Equipment | GET / POST / PUT | `/equipment`, `/equipment/{id}` | BUYER | Equipos del comprador. |
| Equipment | GET / POST | `/refill-history`, `/refill-history/{id}` | BUYER | Historial de recargas. |
| Fulfillment | GET / POST / PUT | `/drivers`, `/drivers/{id}`, `/drivers/provider/{providerId}` | PROVIDER | Conductores. |
| Fulfillment | GET / POST / PUT | `/vehicles`, `/vehicles/{id}`, `/vehicles/provider/{providerId}`, `/vehicles/provider/{providerId}/available` | PROVIDER | Vehículos cisterna y su disponibilidad. |
| Fulfillment | GET / POST | `/deliveries`, `/deliveries/{id}`, `/deliveries/order/{orderId}`, `/deliveries/{id}/complete` | BUYER, PROVIDER | Consulta, registro y cierre de entregas. |
| Payment | POST | `/payment-checkout` | BUYER | Checkout simulado atómico: calcula importes e IGV (18 %) en el servidor, marca la orden como `PAID` y genera el comprobante `SIM-INV-{orderId}`. |
| Payment | GET | `/payments`, `/payments/{id}`, `/payments/order/{orderId}` | BUYER | Historial de pagos. |
| Payment | GET | `/invoices`, `/invoices/{id}`, `/invoices/order/{orderId}` | BUYER | Comprobantes académicos. |
| Notification | GET / POST / PUT / DELETE | `/notifications`, `/notifications/{id}`, `/notifications/buyer/{id}`, `/notifications/provider/{id}` | BUYER, PROVIDER | Notificaciones por segmento. |
| Notification | POST | `/notifications/{id}/read`, `/notifications/buyer/{id}/read-all`, `/notifications/provider/{id}/read-all` | BUYER, PROVIDER | Marcado de lectura individual y masivo. |
| Reporting | GET | `/analytics/buyer-dashboard/{buyerCompanyId}`, `/analytics/buyer/{buyerCompanyId}/{recurso}` | BUYER, PROVIDER | `spending-summary`, `monthly-spending`, `spending-by-provider`, `spending-by-fuel-type`, `spending-by-equipment`; parámetro `year`. |
| Reporting | GET | `/analytics/provider-dashboard/{providerId}`, `/analytics/provider/{providerId}/{recurso}` | BUYER, PROVIDER | `sales-summary`, `revenue-over-time`, `revenue-by-fuel-type`, `orders-by-status`, `customers-by-sector`, `top-customers`; parámetro `year`. |

**Operaciones restringidas para proteger el ciclo de vida:** `POST /orders` y `PUT /orders/{id}` responden `400 Bad Request`, porque las órdenes solo se crean al aprobar una solicitud y cambian de estado mediante las acciones anteriores. La creación directa de pagos y comprobantes (`POST /payments`, `POST /invoices`) queda reservada al rol `ADMIN`; el comprador paga únicamente mediante `/payment-checkout`. Los controladores y servicios comprueban que la empresa del usuario autenticado sea la propietaria del recurso consultado o modificado.

---

#### 5.2.3.7. Software Deployment Evidence for Sprint Review

El despliegue de los Web Services RESTful de FullTank se encuentra **completado, verificado y en operación pública** en la plataforma en la nube **Render**, conectado de forma continua y validada con la Web Application alojada en **Firebase Hosting**.

Para garantizar la sostenibilidad del entorno dentro de los límites del nivel gratuito (Render Free) sin incurrir en costos de almacenamiento persistente de pago, se migró el motor de persistencia a **PostgreSQL 18** gestionado en Render (`fulltank-av2-postgres`, commit `daee12a`). El aprovisionamiento automatizado se rige mediante el Blueprint `render.yaml` (proyecto `fulltank-av2`, entorno `av2`).

**Configuración desplegada y operativa en Render:**

| Recurso | Configuración y Especificaciones de Producción | Estado |
|---|---|:---:|
| `fulltank-av2-api` | Web Service Docker en Linux, región Oregon, puerto interno `10000`, runtime .NET 10 Release, health check configurado en `/health`. **URL pública:** `https://fulltank-av2-api-hqhk.onrender.com` | **Live** (Activo) |
| `fulltank-av2-postgres` | Base de datos relacional PostgreSQL 18 gestionada en Render Free tier, base de datos `fulltank_av2`, usuario `fulltank`. Conexión interna cifrada por SSL (`fromService`). | **Available** (Activo) |
| Variables de Entorno de la API | `ASPNETCORE_ENVIRONMENT=Production`; credenciales de PostgreSQL inyectadas dinámicamente; `TokenSettings__Secret` criptográfico generado por Render; `Cors__AllowedOrigins` configurado para `https://full-tank-964e2.web.app` y `https://full-tank-964e2.firebaseapp.com`; `Database__ApplyMigrationsOnStartup=true`; `Database__SeedDemoData=true`; `AcademicDemo__Enabled=true`; `PaymentSettings__EnableSimulation=true`; `Swagger__Enabled=true`. | **Configurado** |

**Verificación y Evidencias de Despliegue en Producción:**

1. **Health Check verificado en Render (`/health`):**
   La API responde exitosamente con código `HTTP 200` y cuerpo de respuesta `Healthy`, acreditando que el proceso del backend .NET se encuentra en ejecución estable y la conexión con la base de datos PostgreSQL en la nube está activa y migrada:
   - **Endpoint verificado:** `https://fulltank-av2-api-hqhk.onrender.com/health`

<div align="center">
  <img src="../assets/chapter-5/despliegue/health-production.png" alt="Verificación de Health Check HTTP 200 en Render" width="850"/>
  <p><em>Figura 5.2.3.7.1: Verificación del endpoint de salud (/health) de la API RESTful en Render — Respuesta HTTP 200 Healthy en el entorno de producción.</em></p>
</div>

2. **Documentación Swagger UI operativa:**
   La especificación interactiva OpenAPI 3.0 está disponible públicamente en la nube, permitiendo la exploración y prueba en tiempo real de los endpoints:
   - **URL pública de Swagger:** `https://fulltank-av2-api-hqhk.onrender.com/swagger/index.html`

3. **Integración Extremo a Extremo con la Web Application (Firebase Hosting):**
   La aplicación web publicada en Firebase Hosting ([full-tank-964e2.web.app](https://full-tank-964e2.web.app/)) fue compilada y desplegada automáticamente mediante el pipeline de CI/CD de GitHub Actions con las variables `VITE_USE_FAKE_API=false` y `VITE_FULLTANK_API_URL=https://fulltank-av2-api-hqhk.onrender.com/api/v1`.
   El manifiesto de despliegue público `deployment.json` acredita que la aplicación en producción consume de forma efectiva la API real:

<div align="center">
  <img src="../assets/chapter-5/despliegue/deployment-firebase.png" alt="Manifiesto de despliegue en producción deployment.json en Firebase Hosting" width="850"/>
  <p><em>Figura 5.2.3.7.2: Manifiesto de despliegue en producción (deployment.json) en Firebase Hosting — Confirmación de integración con la API de Render (simulatedApi: false).</em></p>
</div>

**Estado de culminación del despliegue:** La totalidad de los Web Services RESTful del Sprint 3 y la base de datos relacional se encuentran plenamente desplegados en Render y sincronizados con el frontend en Firebase Hosting, permitiendo la ejecución integral de las transacciones de compra, despacho y facturación simulada en el entorno de producción.

---

#### 5.2.3.8. Team Collaboration Insights during Sprint

Durante el Sprint 3 el equipo trabajó en el repositorio [Full_Tank_Backend](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend) siguiendo GitFlow con ramas temáticas por Bounded Context (`feat/*`), pruebas (`test/*`) e infraestructura (`build/*`, `chore/*`), integradas en `integration/backend` y liberadas en `main` mediante `release/backend`.

Distribución de commits en `main` al release `daee12a` (**12 de noviembre de 2026**):

| Integrante | Cuenta | Commits de trabajo | Merges de integración | Total | Áreas |
|---|---|:---:|:---:|:---:|---|
| Corvacho Damian, Brayan Alexis | `BralexCD` | 26 | 25 | 51 | Base compartida, IAM, hosting, migración a PostgreSQL 18, MCP DB tools, pruebas y despliegue en Render |
| Mantilla Maldonado, Enrique Manuel | `enrique-mantilla` | 19 | 0 | 19 | Catalog, Inventory, Ordering, persistencia, pruebas de órdenes y Render |
| Huingo Tello, Frank Anthony | `Franz2308` | 17 | 0 | 17 | Equipment, Fulfillment, Notification, pruebas de dominio e imagen Docker |
| Payano Puchuri, Joan Fabricio | `joanfpp2-ai` | 11 | 0 | 11 | Payment, Reporting & Analytics y pruebas de checkout |
| **Total** | — | **73** | **25** | **98** | — |

##### Insights

El análisis de actividad y pulso de desarrollo del repositorio `Full_Tank_Backend` refleja la concentración del esfuerzo en la consolidación de los Web Services y la suite de pruebas unitarias.

##### Contributors

El gráfico de contribuciones confirma la participación activa y balanceada de los integrantes en la implementación de sus respectivos Bounded Contexts y pruebas automatizadas: [Contributors en GitHub](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend/graphs/contributors).

##### Network graph

El grafo de ramas audita la correcta aplicación del flujo GitFlow con ramas temáticas (`feat/*`, `test/*`, `chore/*`) integradas ordenadamente: [Network Graph en GitHub](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend/network).

Principales herramientas de comunicación: GitHub (control de versiones e integración por ramas), WhatsApp (coordinación diaria) y Google Meet (planificación y retrospectiva).

##### Acciones de mejora y compromisos para el Sprint 4 (TB2)

- Integrar cada rama mediante Pull Request con al menos una revisión, como establece la política de 5.1.2, para dejar evidencia de la revisión por pares.
- Completar las brechas del Sprint 3: recuperación de contraseña (TS-02 / US-16), cierre de sesión (TS-03 / US-17), eliminación de equipos (TS-25), eliminación de conductores y vehículos y entrega fallida (TS-17 a TS-19) y exportación de reportes en PDF (TS-27 / US-35).
- Reconciliar los criterios de aceptación de US-08, US-11, TS-04, TS-15 y TS-20 con el flujo implementado de pedidos y pago simulado.
- Distribuir las tareas de backend de forma equitativa entre los integrantes del equipo para asegurar aportes verificables en el repositorio.
- Ejecutar las entrevistas de validación (5.3) sobre la versión integrada y reflejar sus hallazgos en el backlog del Sprint 4.

---

## 5.3. Validation Interviews

### 5.3.1. Diseño de Entrevistas

Para el proceso de validación del incremento de software desarrollado durante los Sprints 1, 2 y 3, se estructuró un conjunto de guías de entrevistas semiestructuradas orientadas a contrastar las hipótesis iniciales de Lean UX frente a la experiencia real de los usuarios al interactuar con el prototipo funcional desplegado en producción ([FullTank Web App](https://full-tank-964e2.web.app/)).

El instrumento se organizó de manera diferenciada para cada uno de los dos segmentos objetivo del modelo de negocio de FullTank:
1. **Segmento 1: Empresas solicitantes de combustible (Compradores)** — Centrado en la exploración de catálogo, cotización, vinculación de maquinaria/equipos, solicitud de abastecimiento y trazabilidad de pedidos.
2. **Segmento 2: Empresas proveedoras de combustible (Proveedores)** — Centrado en la administración de inventario de hidrocarburos, evaluación y aprobación de solicitudes entrantes, asignación de flota (vehículos cisterna y conductores autorizados) y confirmación de entregas logísticas.

A continuación, se detallan las guías de entrevista diseñadas para ambos segmentos:

#### Guía de Validación — Segmento 1: Empresas Solicitantes de Combustible (Compradores)

1. **Percepción de Valor y Usabilidad General:** Al interactuar con el flujo de compra (desde explorar el catálogo y tus equipos hasta emitir una solicitud), ¿cuáles consideras que fueron las pantallas o funciones más claras, intuitivas y que te aportaron mayor valor operativo?
2. **Fricciones y Puntos de Dolor en la Interfaz:** Durante el recorrido por la plataforma, ¿en qué momentos, campos o pantallas sentiste fricción, lentitud o falta de claridad sobre cuál era el siguiente paso a seguir?
3. **Claridad del Modelo de Dominio:** En módulos como la gestión de 'Equipos' (maquinaria/tanques de obra) o los estados del pedido (aprobado, despachado, entregado), ¿identificaste algún término, métrica o componente cuya función dentro de la operativa de tu empresa no haya quedado del todo clara?
4. **Completitud Funcional (Feature Completeness):** Considerando cómo compras combustible en tu empresa (volúmenes en galones/litros, combustible diésel B5 S-50, comprobantes fiscales, autorizaciones internas), ¿qué información crítica sentiste que le falta a la interfaz para cubrir tu ciclo de compra completo?
5. **Confianza Transaccional y Seguridad Operativa:** Al tratarse de compras B2B de alto valor monetario e impacto en la continuidad de sus operaciones, ¿la plataforma te transmite la seguridad, formalidad y transparencia necesarias para autorizar un pedido real? ¿Qué te genera certeza y qué te genera desconfianza?
6. **Eficiencia Operativa frente al Proceso Actual:** Frente a tu gestión actual (llamadas telefónicas, chats de WhatsApp, fotos de váuchers y cuadre manual en Excel), ¿en qué tareas puntuales consideras que FullTank reduce carga administrativa o previene errores humanos?
7. **Intención de Adopción y Reemplazo de Herramientas:** Si tu empresa tuviera acceso operativo a FullTank a partir de mañana, ¿reemplazarías tus canales actuales de compra para abastecer tus obras o flotas mediante este sistema web? ¿Qué facilitaría o impediría esa transición en tu equipo?
8. **Factor Crítico de Éxito (Deal Breaker):** Pensando en una condición indispensable o requisito no negociable para tu área de compras y logística, ¿cuál es esa característica que, de no estar presente o fallar, te obligaría a descartar por completo el uso de la aplicación?
9. **Agilidad en la Generación de Pedidos:** Evaluando la cantidad de pasos, campos y pantallas desde que seleccionas el producto hasta que envías la solicitud, ¿sientes que el flujo es ágil o consideras que en una urgencia operativa en obra seguirías prefiriendo coordinar por llamada o mensaje directo?
10. **Recomendación y Satisfacción Global (NPS Cualitativo):** En una escala de percepción general, ¿recomendarías esta solución web a colegas de logística o empresas contratistas que enfrentan los mismos desafíos de abastecimiento? ¿Cuál sería tu argumento principal?

#### Guía de Validación — Segmento 2: Empresas Proveedoras de Combustible (Proveedores)

1. **Percepción de Valor y Control Operativo:** Al interactuar con el panel de proveedor (actualizar precios y stock, atender solicitudes entrantes y asignar cisternas y conductores), ¿cuáles consideras que fueron las funciones más claras, ordenadas y de mayor utilidad para tu operación logística diaria?
2. **Fricciones y Puntos de Dolor en la Interfaz:** Durante la navegación y ejecución de tareas como proveedor, ¿en qué momentos, tablas o formularios sentiste confusión, pasos redundantes o falta de información crítica para tomar una decisión de despacho?
3. **Claridad del Modelo de Dominio de Fulfillment e Inventario:** En secciones como la gestión de 'Fulfillment' (flota de vehículos, conductores, estados AVAILABLE / ASSIGNED) o las métricas de inventario, ¿identificaste algún término, estado o control cuya función dentro de la operativa de distribución mayorista no haya quedado clara?
4. **Completitud Funcional Normativa y Operativa:** Considerando la operativa real de una distribuidora de combustible (límites de crédito, registro de guía de remisión física/electrónica, certificaciones de choferes, cubicaje de cisternas), ¿qué datos o funcionalidades críticas sentiste que faltan en la plataforma para gestionar tus entregas con total rigurosidad?
5. **Confiabilidad Transaccional en Despachos:** Tratándose de despachos de miles de galones donde cualquier error en la asignación o retraso genera penalidades y reclamos de clientes, ¿el sistema te transmite la robustez y consistencia necesarias para coordinar tus despachos reales por este medio? ¿Qué aspectos te generan confianza o incertidumbre?
6. **Eficiencia en la Programación Logística vs. Proceso Actual:** Frente a tu gestión cotidiana actual (hojas de cálculo de programación de ruta, cruce manual de llamadas con choferes, confirmaciones dispersas por WhatsApp), ¿en qué procesos específicos consideras que esta plataforma optimizaría tus tiempos de despacho y control de inventario?
7. **Intención de Adopción e Integración Comercial:** Si los clientes contratistas y empresas comenzaran a emitir sus requerimientos por FullTank, ¿tu empresa adoptaría la plataforma como su canal oficial de recepción de pedidos y programación de flota? ¿Cuáles serían los principales factores impulsores o frenos para implementarla?
8. **Factor Crítico de Éxito (Deal Breaker):** Pensando en una exigencia operativa o legal no negociable para una empresa distribuidora de combustible, ¿cuál es esa funcionalidad o salvaguarda que, de no estar resuelta en la plataforma, te impediría utilizarla comercialmente?
9. **Impacto en la Organización y Trazabilidad:** Al centralizar en una sola plataforma la recepción de pedidos, la disponibilidad de inventario, la asignación de recursos logísticos y el histórico de entregas cerradas, ¿consideras que reduce significativamente el riesgo de desorden operativo y traspapeleo frente a tus métodos habituales?
10. **Recomendación y Satisfacción Global (NPS Cualitativo):** En una escala de percepción general, ¿recomendarías esta herramienta a otras empresas distribuidoras o estaciones mayoristas del sector que buscan digitalizar su canal corporativo? ¿Cuál sería la ventaja clave que destacarías?

### 5.3.2. Registro de Entrevistas

Las entrevistas de validación se realizan con **3 a 5 representantes por segmento (6 a 10 en total)**. Cada entrevistado usa la Web Application con una cuenta demo de su segmento, ejecuta un conjunto de tareas mientras piensa en voz alta y, al final, responde las preguntas de la guía de 5.3.1. Cada registro sigue el formato de la sección [2.2.2](chapter2.md#222-registro-de-entrevistas) e incluye la grabación, las tareas realizadas y los hallazgos.

**Segmento 1: Empresas solicitantes de combustible**

- Entrevista 1:

| Campo | Detalle |
|---|---|
| **Nombre entrevistado** | Daniel Angelo Siqueiros Cruz |
| **Edad** | 21 |
| **Distrito** | Los Olivos, Lima |
| **Cargo y empresa** | Asistente de logística y almacén en una empresa constructora mediana de Lima Norte (comprador). Fue entrevistado también en la etapa de Needfinding ([2.2.2](chapter2.md#222-registro-de-entrevistas)). |
| **Fecha** | 12 de noviembre de 2026 |
| **Modalidad** | Google Meet, con la pantalla del entrevistado compartida |
| **Aplicación evaluada** | Web Application publicada en Firebase Hosting ([full-tank-964e2.web.app](https://full-tank-964e2.web.app/iam/login)), versión de demostración con API simulada y cuenta demo de comprador |
| **Inicio del video** | 00:00 |
| **Fin del video** | 20:06 |
| **Link del video** | https://upcedupe-my.sharepoint.com/:v:/g/personal/u202318620_upc_edu_pe/IQD0d-oI1gIDTZiCz0JJZ-RtAa51OEsD6ojaPZxYjaDgspY?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=oKir2m |
| **Foto entrevista** | <img src="../assets/chapter-5/validacion/entrevista-daniel-siqueiros.webp" alt="Captura de la entrevista de validación con Daniel Angelo Siqueiros Cruz en Google Meet, con la pantalla de inicio de sesión de FullTank compartida" width="300"/> |
| **Tareas realizadas** | 1) Iniciar sesión con la cuenta demo de comprador (02:22). 2) Identificar en el dashboard los pedidos en curso (03:11). 3) Ubicar el equipo con menor nivel de combustible y solicitar su recarga desde el catálogo (03:39). 4) Registrar un pedido para ese equipo (04:41). 5) Consultar el estado del pedido (06:36). 6) Pagar una orden pendiente con el pago simulado y descargar la factura (07:13). 7) Revisar las notificaciones (11:38). 8) Obtener el resumen mensual de gasto por equipo (12:26). Preguntas de validación desde 13:09 y cierre desde 19:12. |
| **Puntuación de facilidad de uso** | 8 de 10 |
| **Resumen** | <p>Daniel mantiene el mismo proceso descrito en Needfinding: coordina los pedidos por un grupo de WhatsApp con el proveedor, su jefe transfiere desde la banca móvil y envía la captura del voucher al chat, y él pasa esas imágenes a un Excel compartido con el almacén. A fin de mes tardó cerca de dos horas en cuadrar facturas con capturas borrosas, y sigue llamando al chofer para saber si el camión ya salió de la planta.</p><p>Completó las ocho tareas. Necesitó ayuda para elegir la cuenta demo en el inicio de sesión. Encontró sin dificultad las órdenes activas y el equipo con menor nivel, y valoró que el catálogo solo le permitiera comprar el combustible compatible con su máquina. Al registrar el pedido, el sistema rechazó los 1,400 litros porque superaban la capacidad restante del equipo; entendió el motivo solo cuando el entrevistador le explicó que faltaban 20 litros. En el estado del pedido solo vio «Pendiente» y no pudo saber si el camión había salido ni cuándo llegaría. Pagó con el formulario simulado y descargó la factura en PDF, que salió en dos hojas; el pago recién hecho no apareció en el historial de pagos. Las notificaciones le resultaron claras, pero el reporte de gasto no se puede imprimir, algo que su jefe necesita.</p><p>Considera las notificaciones la función más útil y el reporte de analítica el mayor ahorro de tiempo frente a ordenar capturas de transferencias. El límite de compra según la capacidad del equipo le da confianza para no pedir de más. Señaló textos en inglés en la interfaz en español. Haría por la aplicación incluso un pedido urgente y la recomendaría a otras constructoras por ser intuitiva, aunque al inicio seguiría usando WhatsApp. Dejaría de usarla si los envíos llegan retrasados sin explicación, por lo que lo primero que pide mejorar es ver la ubicación y el tiempo estimado del pedido, y que las facturas aparezcan en el historial apenas se paga.</p> |

- Entrevista 2:

| Campo | Detalle |
|---|---|
| **Nombre entrevistado** | Carlos Gutierrez |
| **Edad** | 20 |
| **Distrito** | Ate, Lima |
| **Cargo y empresa** | Coordinador de compras y abastecimiento en una empresa de transporte y distribución logística en Lima Este (comprador). Fue entrevistado también en la etapa de Needfinding ([2.2.2](chapter2.md#222-registro-de-entrevistas)). |
| **Fecha** | 13 de noviembre de 2026 |
| **Modalidad** | Microsoft Teams, con la pantalla del entrevistado compartida |
| **Aplicación evaluada** | Web Application publicada en Firebase Hosting ([full-tank-964e2.web.app](https://full-tank-964e2.web.app/iam/login)), versión integrada conectada a la API RESTful en Render con cuenta demo de comprador |
| **Inicio del video** | 00:00 |
| **Fin del video** | 18:24 |
| **Link del video** | https://upcedupe-my.sharepoint.com/:v:/g/personal/u202319057_upc_edu_pe/IQDMMhBaDW31QaSwAxP9_ZlXAVUCbf_fgjEA5JrOcAoHLCg?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=4DLQ8d |
| **Foto entrevista** | <img src="../assets/chapter-5/validacion/entrevista-carlos-gutierrez.webp" alt="Captura de la entrevista de validación con Carlos Gutierrez en Microsoft Teams, con la plataforma FullTank compartida" width="300"/> |
| **Tareas realizadas** | 1) Inicio de sesión con la cuenta demo de comprador institucional (01:45). 2) Exploración del catálogo de proveedores y selección de combustible Diésel B5 S-50 (02:50). 3) Verificación de la flota vehicular y nivel de combustible en el módulo de Equipos (04:15). 4) Creación de solicitud de abastecimiento masivo para cisterna de transporte (05:40). 5) Seguimiento del estado del pedido en la bandeja transaccional (08:12). 6) Ejecución del flujo de checkout y simulación de pago con emisión de comprobante SIM-INV (10:05). 7) Revisión de alertas operativas y centro de notificaciones (13:20). 8) Consulta de analítica y reporte mensual de gastos por unidad (14:45). Preguntas de validación cualitativa desde 15:30 y retroalimentación final (17:50). |
| **Puntuación de facilidad de uso** | 8.5 de 10 |
| **Resumen** | <p>Carlos evaluó la plataforma desde su perspectiva de coordinador de compras de una flota de transporte pesado con un volumen mensual de 280,000 litros. Destacó de inmediato la solución al principal problema que reportó en Needfinding: la dispersión de compras en hojas de cálculo y llamadas telefónicas a múltiples proveedores para verificar precios y disponibilidad. La capacidad de explorar el catálogo de proveedores con precios unitarios actualizados y filtrar por combustible compatible le pareció un avance crítico que agilizaría las cotizaciones en su empresa.</p><p>Completó satisfactoriamente las ocho tareas asignadas. Durante el flujo de creación de solicitud, valoró que el sistema valide la capacidad del tanque de la cisterna evitando sobrellenados accidentales. No obstante, señaló que en flotas grandes de transporte se requiere poder agrupar o etiquetar las unidades por sede o ruta de distribución en lugar de una lista continua. Al consultar el estado del pedido, coincidió plenamente en que ver únicamente el estado «Pendiente» sin un tiempo estimado de arribo (ETA) o ubicación de la cisterna genera incertidumbre, obligándolo a seguir dependiendo de llamadas al despachador. En la pasarela de pago, validó positivamente el desglose automático del IGV (18%) y la generación inmediata del comprobante académico, aunque solicitó poder exportar el historial de compras directamente a formato Excel/CSV para integrarlo con el software contable de su empresa.</p><p>Como balance general, Carlos otorgó una calificación de 8.5/10 a la plataforma, catalogándola como una herramienta profesional, robusta y con una curva de aprendizaje mínima para el personal de logística. Considera que las notificaciones automáticas y el módulo de analítica reducirían hasta en un 60% el tiempo dedicado a conciliar comprobantes a fin de mes. Recomienda priorizar para la versión final la visualización de la ruta de entrega en tiempo real y la compatibilidad con exportaciones contables en Excel.</p> |

- Entrevista 3:

| Campo | Detalle |
|---|---|
| **Nombre entrevistado** | Alessandro Gonzales |
| **Edad** | 21 |
| **Distrito** | Santiago de Surco, Lima |
| **Cargo y empresa** | Encargado de gestión de abastecimiento y coordinación logística de combustible en el sector energético y de obra civil (comprador). Fue entrevistado también en la etapa de Needfinding ([2.2.2](chapter2.md#222-registro-de-entrevistas)). |
| **Fecha** | 14 de noviembre de 2026 |
| **Modalidad** | Videollamada, con la plataforma FullTank compartida en vivo |
| **Aplicación evaluada** | Web Application publicada en Firebase Hosting ([full-tank-964e2.web.app](https://full-tank-964e2.web.app/equipment)), versión integrada conectada a la API RESTful en Render con cuenta demo de comprador (`Transportes del Sur S.A.`) |
| **Inicio del video** | 00:00 |
| **Fin del video** | 09:43 |
| **Link del video** | *Pendiente de publicación en Microsoft Stream (grabación local: `2026-11-14 22-20-13-editado.mp4`)* |
| **Foto entrevista** | <img src="../assets/chapter-5/validacion/entrevista-alessandro-gonzales.webp" alt="Captura de la entrevista de validación con Alessandro Gonzales mostrando el módulo Equipment de FullTank" width="300"/> |
| **Tareas realizadas** | 1) Revisión del módulo Equipment con generadores, excavadoras y barras de nivel de combustible (00:15). 2) Exploración del catálogo de distribuidoras y simulación de nueva solicitud seleccionando equipo, cantidad y fecha (00:30, 01:24, 03:13). 3) Revisión de solicitudes y detalle de orden aprobada con nombre del chofer y placa del cisterna en Ordering (04:08). 4) Verificación del centro de notificaciones ante cambios de estado (05:07). 5) Consulta del módulo de pagos y archivo de comprobantes digitales (06:09). 6) Revisión del panel principal del comprador (07:11). 7) Consulta del módulo de Reports & Analytics para consumo mensual por equipo (07:52). Preguntas de validación entre 00:39 y 09:27. |
| **Puntuación de facilidad de uso** | 8 de 10 |
| **Resumen** | <p>Alessandro evaluó el flujo completo desde la perspectiva de logística en obra civil y operación de maquinaria pesada (generadores y excavadoras). Destacó de inmediato la utilidad del módulo Equipment y sus barras de capacidad para evitar que las máquinas trabajen en reserva o queden paralizadas, así como la rapidez para generar un pedido directamente desde el Fuel Catalog. Consideró que el formulario de solicitud es corto, ágil y mucho más seguro que enviar audios por WhatsApp, los cuales el proveedor muchas veces no escucha a tiempo.</p><p>Durante el recorrido identificó mejoras puntuales para la operación en campo: en el catálogo con múltiples distribuidoras sugirió resaltar qué proveedor ofrece el menor tiempo de entrega (03:51); en el detalle de la orden consideró insuficiente mostrar solo el nombre del chofer y la placa del cisterna, solicitando un botón directo con el teléfono del conductor para coordinar el ingreso a obra y referencias de acceso (04:45). Asimismo, valoró positivamente las notificaciones en tiempo real porque brindan certeza de aprobación y ruta (05:48), y resaltó que archivar los comprobantes digitales en Payments elimina las pérdidas y daños habituales de los váuchers físicos (06:45).</p><p>Como condición crítica (*deal breaker*) señaló la obligatoriedad de recibir alertas inmediatas ante falta de stock o cancelación del proveedor para ubicar rápidamente otra distribuidora sin detener la producción en obra (07:31). Confirmó que su empresa adoptaría FullTank desde el primer día porque alivia la carga de almacén y permite a los supervisores consultar el consumo mensual por máquina desde laptop o celular sin pedir reportes por correo (08:29). Otorgó una puntuación global de 8/10 y recomendó la plataforma para contratistas y constructoras.</p> |

**Segmento 2: Empresas proveedoras de combustible**

| Campo | Detalle |
|---|---|
| **Nombre entrevistado** | |
| **Edad** | |
| **Distrito** | |
| **Cargo y empresa** | |
| **Fecha** | |
| **Inicio del video** | |
| **Fin del video** | |
| **Link del video** | |
| **Foto entrevista** | |
| **Tareas realizadas** | Por ejemplo: iniciar sesión, actualizar inventario y precios, aprobar una solicitud, asignar vehículo y conductor, despachar y revisar reportes. |
| **Resumen** | |

**Síntesis de hallazgos**

La tabla se actualiza a medida que se registran nuevas entrevistas. La frecuencia indica cuántos entrevistados mencionaron u ocasionaron el hallazgo; el número entre paréntesis es el minuto del video de la Entrevista 1 del Segmento 1.

| # | Hallazgo | Segmento | Frecuencia | Historia o artefacto afectado | Acción propuesta para el Sprint 4 |
|:---:|---|---|:---:|---|---|
| 1 | El estado del pedido solo muestra «Pendiente»; no indica si el despacho salió ni cuándo llegará (E1: 06:39; E2: 08:15). Es la condición que haría abandonar la aplicación. | Solicitante | 2 | US-06, US-43, US-12 | Mostrar la línea de tiempo de estados con fecha y hora de cada cambio y la hora estimada de llegada; evaluar el seguimiento de la ubicación del despacho para TB2. |
| 2 | El pago recién realizado no aparece en el historial de pagos ni su factura (11:17, 13:46). | Solicitante | 1 | US-08, TS-21 | Actualizar el historial con el pago y el comprobante apenas termina el checkout, usando los datos persistidos por la API. |
| 3 | La factura descargada en PDF ocupa dos hojas (10:41). | Solicitante | 1 | US-08 | Ajustar el formato de impresión del comprobante a una sola hoja. |
| 4 | El reporte de gasto no se puede imprimir ni exportar; se requiere en físico o en formato Excel/CSV para conciliación contable (E1: 12:45; E2: 15:10). | Solicitante | 2 | US-35, TS-27 | Implementar la exportación del reporte a PDF con sus gráficos y descarga de data tabulada en CSV/Excel. |
| 5 | Hay textos en inglés cuando la interfaz está en español (E1: 14:12; E2: 06:10). | Solicitante | 2 | US-39 | Completar las traducciones de i18n en las vistas afectadas. |
| 6 | El mensaje de cantidad mayor a la capacidad restante se entendió solo tras la explicación del entrevistador (05:51). | Solicitante | 1 | US-05 | Mostrar la capacidad restante junto al campo de cantidad y ofrecer completar el tanque con un clic. |
| 7 | No quedó claro qué cuenta demo usar ni qué parte del texto copiar al iniciar sesión (02:29). | Solicitante | 1 | US-15 | Presentar las cuentas demo con botones «Usar cuenta de comprador / proveedor». |
| 8 | Preguntó si puede guardar la tarjeta para no ingresarla en cada compra (08:33). | Solicitante | 1 | US-08 | Fuera del alcance actual: el pago es simulado y no se almacenan datos de tarjetas. Se registra para una futura integración real. |
| 9 | En flotas extensas de transporte, la selección de equipos requiere filtros por sede operativa o placa vehicular para agilizar la asignación en compras masivas (E2: 04:30). | Solicitante | 1 | US-05, US-23 | Incorporar filtros por placa/sede y buscador predictivo en el selector de equipos y maquinaria. |
| 10 | En el catálogo con varias distribuidoras, no se destaca visualmente cuál proveedor ofrece la entrega más rápida (E3: 03:51). | Solicitante | 1 | US-05 | Mostrar tiempo estimado de entrega (SLA) y una etiqueta visual de «Entrega más rápida» en las tarjetas del catálogo. |
| 11 | El detalle del pedido muestra el nombre del chofer y la placa del cisterna, pero carece de un botón con el teléfono directo del conductor para coordinar el ingreso a obra (E3: 04:45). | Solicitante | 1 | US-26, US-45, US-49 | Incluir el número telefónico del conductor asignado con botón de contacto directo en el detalle del despacho. |
| 12 | Falta una alerta prioritaria diferenciada cuando el proveedor no tiene stock o cancela el pedido, condición crítica para reasignar proveedor sin parar la maquinaria (E3: 07:31). | Solicitante | 1 | US-29, US-12 | Destacar las alertas de rechazo, cancelación o quiebre de stock con alta prioridad y acceso rápido a proveedores alternativos. |

**Aspectos validados positivamente:** las notificaciones en tiempo real (función más valorada para certeza de aprobación y ruta), el monitoreo visual de niveles en Equipment para evitar trabajo en reserva, el filtro del catálogo por compatibilidad y precios unitarios transparentes, el límite de compra según capacidad del tanque, el archivo digital de comprobantes frente al deterioro/pérdida de váuchers físicos, el reporte analítico consultable por supervisores sin correos manuales y la facilidad general de uso (calificación promedio de 8.17/10 entre los tres compradores entrevistados).

### 5.3.3. Evaluaciones según heurísticas

La evaluación de usabilidad se realizó aplicando las **10 heurísticas de usabilidad de Jakob Nielsen** sobre los recorridos guiados de la Web Application integrada ([full-tank-964e2.web.app](https://full-tank-964e2.web.app/)) a partir de las tres entrevistas de validación registradas del Segmento 1 (`Daniel Angelo Siqueiros Cruz`, `Carlos Gutierrez` y `Alessandro Gonzales`). Las tareas 5 y 6 (flujo exclusivo de proveedor) quedan previstas para ampliarse una vez registradas las entrevistas del Segmento 2. Cada problema se califica en la escala de severidad de `0` (no es un problema) a `4` (catástrofe de usabilidad):

| Campo | Detalle |
|---|---|
| **Carrera** | Ingeniería de Software |
| **Curso** | 1ASI0730 Aplicaciones Web |
| **Sección** | 16129 |
| **Profesor** | Sánchez Seña, Alberto Wilmer |
| **Auditor** | Equipo FuelPoint — Frank Anthony Huingo Tello, Brayan Alexis Corvacho Damian, Enrique Manuel Mantilla Maldonado y Joan Fabricio Payano Puchuri |
| **Cliente(s)** | Daniel Angelo Siqueiros Cruz, Carlos Gutierrez y Alessandro Gonzales *(Segmento 1: Empresas solicitantes de combustible — corte al 14/11/2026)* |
| **Sitio o aplicación evaluada** | FullTank Web Application ([https://full-tank-964e2.web.app/](https://full-tank-964e2.web.app/)) |

**Tareas evaluadas**

| # | Tarea | Segmento | Estado de auditoría |
|:---:|---|---|:---:|
| 1 | Iniciar sesión y registrar una empresa | Ambos | Evaluada (Solicitante) |
| 2 | Registrar una solicitud de combustible para un equipo | Solicitante | Evaluada |
| 3 | Consultar el estado y el detalle de un pedido | Solicitante | Evaluada |
| 4 | Confirmar la recepción y pagar un pedido (checkout simulado) | Solicitante | Evaluada |
| 5 | Actualizar inventario y precios | Proveedor | Pendiente de entrevistas Seg. 2 |
| 6 | Aprobar una solicitud y asignar vehículo y conductor | Proveedor | Pendiente de entrevistas Seg. 2 |
| 7 | Revisar notificaciones y reportes | Ambos | Evaluada (Solicitante) |

**Escala de severidad:** `0` = no es un problema; `1` = problema cosmético; `2` = problema menor; `3` = problema mayor; `4` = catástrofe de usabilidad.

**Tabla resumen**

| # | Problema | Escala de severidad | Heurística o principio violado |
|:---:|---|:---:|---|
| 1 | Ausencia de línea de tiempo de despacho, ETA y botón de contacto directo con el conductor en pedidos activos | 3 | H1: Visibilidad del estado del sistema |
| 2 | Reportes analíticos sin exportación a PDF/Excel ni impresión directa, y comprobante de pago dividido en dos páginas | 3 | H7: Flexibilidad y eficiencia de uso |
| 3 | Falta de alerta prioritaria ante quiebre de stock/cancelación y retardo en reflejar pagos recién confirmados en el historial | 3 | H1: Visibilidad del estado del sistema / H9: Reconocer, diagnosticar y recuperarse de errores |
| 4 | Mezcla de etiquetas en inglés dentro de la interfaz en español y marca residual «PrimeFuel» en el inicio de sesión | 2 | H4: Consistencia y estándares |
| 5 | Validación reactiva de capacidad restante del equipo y falta de filtros por placa o sede en el selector | 2 | H5: Prevención de errores |
| 6 | Credenciales demo presentadas en texto plano sin botones de autocompletado de un clic | 2 | H7: Flexibilidad y eficiencia de uso |
| 7 | Presencia de proveedores de prueba sin productos y ausencia de indicador de menor tiempo de entrega en el catálogo | 2 | H8: Diseño estético y minimalista / H2: Coincidencia entre el sistema y el mundo real |

**Descripción de problemas**

#### Problema 1 — Ausencia de línea de tiempo, ETA y contacto directo con el conductor en pedidos activos
- **Heurística violada:** H1 — Visibilidad del estado del sistema.
- **Severidad:** `3` (Problema mayor).
- **Evidencia en entrevistas:** E1 (`06:39`), E2 (`08:15`), E3 (`04:45`).
- **Descripción:** En el listado y detalle de órdenes (`My Fuel Requests`), la interfaz solo expone un estado genérico («Pendiente» / aprobado) y los datos básicos del conductor y placa sin mostrar la evolución temporal (aprobación, salida de planta, en ruta), el tiempo estimado de arribo (ETA) ni un acceso rápido al teléfono del chofer. Esto obliga a los compradores a recurrir nuevamente a llamadas o WhatsApp para confirmar si la cisterna llegará a obra y coordinar el ingreso, además de presentar recorte horizontal en columnas derechas de la tabla.
- **Captura de pantalla:**

<div align="center">
  <img src="../assets/chapter-5/ejecucion-tb1/solicitudes-desktop.png" alt="Vista de solicitudes y pedidos del comprador sin línea de tiempo ni contacto directo del conductor" width="750"/>
  <p><em>Figura 5.3.3.1: Listado de solicitudes en Ordering sin línea de tiempo de despacho, ETA ni enlace directo al conductor asignado.</em></p>
</div>

- **Recomendación:** Incorporar en el detalle del pedido una línea de tiempo cronológica con marca horaria por hito, mostrar el ETA calculado y añadir junto al nombre del conductor asignado su número telefónico con acción directa de llamada/WhatsApp, ajustando además el ancho responsivo de la tabla.

#### Problema 2 — Reportes sin exportación PDF/Excel ni impresión y factura PDF extendida en dos hojas
- **Heurística violada:** H7 — Flexibilidad y eficiencia de uso (y H8 — Diseño estético y minimalista en formato de impresión).
- **Severidad:** `3` (Problema mayor).
- **Evidencia en entrevistas:** E1 (`10:41`, `12:45`), E2 (`15:10`).
- **Descripción:** Aunque los entrevistados valoraron las métricas de **Reports & Analytics** y el desglose tributario de los comprobantes en **Payment**, el módulo de reportes carece de botones para imprimir o exportar el resumen mensual en PDF/Excel/CSV para conciliación contable y gerencial (mostrando además promedios con tres decimales como `S/ 4,788.633`). Adicionalmente, la factura generada tras pagar se extiende innecesariamente a dos páginas PDF.
- **Captura de pantalla:**

<div align="center">
  <img src="../assets/chapter-5/ejecucion-tb1/reportes-comprador-desktop.png" alt="Módulo Reports & Analytics del comprador sin botones de exportación PDF o Excel/CSV" width="750"/>
  <p><em>Figura 5.3.3.2: Panel Reports & Analytics sin acciones de exportación ni impresión, y con promedios monetarios sin redondeo estándar a dos decimales.</em></p>
</div>

- **Recomendación:** Implementar botones de exportación en PDF (gráficos y resumen) y descarga en CSV/Excel para contabilidad, redondear todos los importes monetarios a dos decimales (`0.00`) y compactar la plantilla de impresión del comprobante `SIM-INV` a una única página.

#### Problema 3 — Falta de alerta prioritaria por quiebre de stock/cancelación y desfase en historial tras pagar
- **Heurística violada:** H1 — Visibilidad del estado del sistema y H9 — Ayudar a los usuarios a reconocer, diagnosticar y recuperarse de errores.
- **Severidad:** `3` (Problema mayor).
- **Evidencia en entrevistas:** E1 (`11:17`, `13:46`), E3 (`07:31`).
- **Descripción:** Tras confirmar un pago en el flujo de checkout simulado de **Payments**, la actualización hacia la pestaña *Payment History* y el listado de facturas no se refleja de inmediato sin recargar o navegar fuera de la vista. Asimismo, en el centro de notificaciones todos los avisos presentan el mismo peso visual sin diferenciar una alerta crítica (como falta de stock o cancelación del proveedor) que requiere reasignar el pedido de inmediato para no detener la operación en obra.
- **Captura de pantalla:**

<div align="center">
  <img src="../assets/chapter-5/ejecucion-tb1/pagos-desktop.png" alt="Módulo Payments mostrando órdenes pendientes y enlace a Payment History" width="750"/>
  <p><em>Figura 5.3.3.3: Vista de Payments donde tras ejecutar el pago simulado el comprobante no se refresca de inmediato en Payment History.</em></p>
</div>

- **Recomendación:** Rehidratar el store y la vista de *Payment History* automáticamente al confirmar el pago desde la API, e introducir severidades visuales (alerta crítica en rojo/ámbar) en **Notifications** cuando un pedido sea rechazado o cancelado, incluyendo un enlace directo hacia proveedores alternativos compatibles.

#### Problema 4 — Mezcla de idioma inglés/español en la interfaz y referencia residual «PrimeFuel»
- **Heurística violada:** H4 — Consistencia y estándares.
- **Severidad:** `2` (Problema menor).
- **Evidencia en entrevistas:** E1 (`14:12`), E2 (`06:10`), y observación directa en las capturas de validación (E3).
- **Descripción:** Pese a contar con el conmutador `EN | ES`, múltiples encabezados de navegación, botones de acción (`Switch segment`, `Request Refill`, `Pay now`), mensajes de advertencia y descripciones mantienen literales en inglés cuando el usuario navega con perfil hispanohablante, y la pantalla de inicio de sesión todavía muestra la leyenda «B2B Fuel Distribution Platform by PrimeFuel» en lugar de la identidad vigente **FuelPoint**.
- **Captura de pantalla:**

<div align="center">
  <img src="../assets/chapter-5/ejecucion-tb1/login-desktop.png" alt="Pantalla de inicio de sesión con texto en inglés y marca residual PrimeFuel" width="600"/>
  <p><em>Figura 5.3.3.4: Pantalla de inicio de sesión con textos en inglés y referencia residual «PrimeFuel».</em></p>
</div>

- **Recomendación:** Completar los diccionarios i18n (`es.json` / `en.json`) en todos los módulos y fijar español como idioma predeterminado para usuarios locales, actualizando además el texto de marca de inicio de sesión y registro a **FuelPoint**.

#### Problema 5 — Validación reactiva de capacidad restante del tanque y ausencia de filtros en flotas grandes
- **Heurística violada:** H5 — Prevención de errores.
- **Severidad:** `2` (Problema menor).
- **Evidencia en entrevistas:** E1 (`05:51`), E2 (`04:30`).
- **Descripción:** En el formulario lateral de nueva solicitud (`Fuel Catalog -> New Request`), el campo `Quantity` no muestra en línea los litros disponibles hasta completar la capacidad del equipo seleccionado ni ofrece un atajo para llenar el tanque. En consecuencia, el solicitante solo descubre que excedió el límite cuando el sistema rechaza el envío. Además, en flotas con numerosas unidades, el selector `Equipment (optional)` lista todos los equipos de forma plana sin filtros por placa vehicular o sede operativa.
- **Captura de pantalla:**

<div align="center">
  <img src="../assets/chapter-5/ejecucion-tb1/nueva-solicitud-desktop.png" alt="Formulario de nueva solicitud sin indicador de capacidad restante junto a Quantity ni filtro de flota" width="750"/>
  <p><em>Figura 5.3.3.5: Panel de solicitud sin mostrar la capacidad restante junto al campo Quantity ni buscador por placa o sede.</em></p>
</div>

- **Recomendación:** Mostrar dinámicamente la capacidad restante disponible (por ejemplo, `Máximo disponible: 1,380 L`) debajo de `Quantity` junto con un botón «Completar tanque», e incorporar buscador predictivo y filtro por sede/placa en el selector de equipos.

#### Problema 6 — Credenciales demo mostradas como texto plano sin botones de acceso directo
- **Heurística violada:** H7 — Flexibilidad y eficiencia de uso.
- **Severidad:** `2` (Problema menor).
- **Evidencia en entrevistas:** E1 (`02:29`).
- **Descripción:** En la pantalla de login (`Figura 5.3.3.4`), las credenciales de demostración se muestran dentro de una caja informativa en texto corrido (`buyer: logistics@transportesdelsur.com · provider: dispatch@petroandes.com (password: 123456)`), lo cual generó dudas al primer usuario sobre qué correo correspondía a su rol y obligó a copiar manualmente usuario y clave.
- **Recomendación:** Reemplazar el bloque informativo de texto plano por dos botones claros de autocompletado de un clic («Usar cuenta demo de comprador» y «Usar cuenta demo de proveedor») o etiquetas copiables independientes.

#### Problema 7 — Ruido visual por registros de prueba y falta de indicador de rapidez de entrega en el catálogo
- **Heurística violada:** H8 — Diseño estético y minimalista y H2 — Coincidencia entre el sistema y el mundo real.
- **Severidad:** `2` (Problema menor).
- **Evidencia en entrevistas:** E3 (`03:51`) e inspección de catálogo en vivo.
- **Descripción:** El módulo **Fuel Catalog** exhibe tarjetas de prueba con datos incompletos o informales (`ExaPe`, `eqe`, `pepe`, con `0 PRODUCTS` y `S/ 0.00`) mezcladas con proveedores reales, generando desconfianza visual y ruido en la comparación. Asimismo, las tarjetas no indican el tiempo estimado de despacho ni resaltan qué distribuidora ofrece la entrega más rápida, criterio señalado como prioritario para pedidos urgentes en obra.
- **Captura de pantalla:**

<div align="center">
  <img src="../assets/chapter-5/ejecucion-tb1/catalogo-desktop.png" alt="Catálogo de proveedores mostrando registros de prueba sin productos y sin indicador de tiempo de entrega" width="750"/>
  <p><em>Figura 5.3.3.6: Vista del catálogo de combustible con registros de prueba (ExaPe, eqe, pepe) y sin etiqueta de tiempo estimado de entrega.</em></p>
</div>

- **Recomendación:** Filtrar o depurar de los entornos públicos de validación los proveedores sin productos activos (`0 PRODUCTS`) y añadir un indicador visible de tiempo estimado de entrega (SLA) con una insignia destacada para el proveedor de despacho más rápido.

## 5.4. Video About-the-Product

El video About-the-Product presenta FullTank a los dos segmentos objetivo: el problema que resuelve, la propuesta de valor y un recorrido breve por la Landing Page y la Web Application. Su duración está comprendida entre **1 y 3 minutos**, disponible e incrustado en la Landing Page:

| Campo | Detalle |
|---|---|
| **Nombre del archivo** | `upc-pre-202620-1asi0730-16129-fuelpoint-about-the-product.mp4` |
| **Duración** | `02:13` |
| **Enlace de publicación** | [YouTube (Público / Incrustado)](https://www.youtube.com/watch?v=Pu_9CAwoQ9k) · [Microsoft Stream (Institucional UPC)](https://upcedupe-my.sharepoint.com/:v:/g/personal/u202319057_upc_edu_pe/IQCPKLBLwm1dRqTXFocr_NDLAc-UL3_xtE5YgzoztbDQ6V4?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=dADcmL) |
| **Ubicación en la Landing Page** | [FullTank Landing Page (`#como-funciona`)](https://1asi0730-2620-16129-g1-fuelpoint.github.io/Full_Tank_Landing_Page/#como-funciona) *(reproductor YouTube incrustado en vivo)* |

## 5.5. Video About-the-Team

El video About-the-Team presenta a los integrantes de FuelPoint, su rol en el proyecto y el proceso de trabajo colaborativo seguido en los sprints, publicado e incrustado en la Landing Page:

| Campo | Detalle |
|---|---|
| **Nombre del archivo** | `upc-pre-202620-1asi0730-16129-fuelpoint-about-the-team.mp4` |
| **Duración** | |
| **Enlace de publicación** | |
| **Ubicación en la Landing Page** | |

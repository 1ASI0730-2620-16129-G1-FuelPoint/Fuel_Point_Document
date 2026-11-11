<div align="center">
  <img src="logo_upc.PNG" alt="Logo UPC" width="180">
  <p><strong>UNIVERSIDAD PERUANA DE CIENCIAS APLICADAS</strong></p>
  <p>FACULTAD DE INGENIERÍA</p>
  <p>CARRERA DE INGENIERÍA DE SOFTWARE</p>
  <br>
  <p><strong>1ASI0730 — APLICACIONES WEB</strong></p>
  <p><strong>SECCIÓN:</strong> 16129</p>
  <p><strong>DOCENTE:</strong> Sánchez Seña, Alberto Wilmer</p>
  <br>
  <h1>INFORME DE AVANCE DEL TRABAJO FINAL (AV2)</h1>
  <br>
  <p><strong>STARTUP:</strong> FuelPoint</p>
  <p><strong>PRODUCTO:</strong> FullTank</p>
  <br>
  <p><strong>RELACIÓN DE INTEGRANTES:</strong></p>

  | Código | Apellidos y Nombres |
  |---|---|
  | U20231A257 | Corvacho Damian, Brayan Alexis |
  | U202319057 | Huingo Tello, Frank Anthony |
  | U202318620 | Payano Puchuri, Joan Fabricio |
  | U20231B842 | Mantilla Maldonado, Enrique Manuel | 
  | U202219040 | Carhuayal Suarez, Joan Salvador | 

  <br>
  <p><strong>CICLO ACADÉMICO:</strong> 2026-20</p>
  <p><strong>FECHA:</strong> Noviembre de 2026</p>
</div>

---

## Registro de Versiones del Informe

| Versión | Fecha | Autor | Descripción de modificación |
|---|---|---|---|
| **0.1.0** | 2026-08-28 | Equipo FuelPoint | Versión inicial del informe para el hito AV1. Se estructuró la carátula, perfil de la startup (FuelPoint), perfiles de integrantes, antecedentes con 5W2H, supuestos de Lean UX, especificación de requisitos iniciales y la documentación del Sprint 1 para la Landing Page. |
| **0.2.0** | 2026-09-12 | Equipo FuelPoint | Incorporación del Capítulo II: registro de entrevistas grabadas con clientes y proveedores de combustible, análisis estadístico de hallazgos, User Personas en UXPressia, User Task Matrix, User Journey Mapping As-Is y sesión de Big Picture EventStorming. |
| **0.3.0** | 2026-09-26 | Equipo FuelPoint | Incorporación del Capítulo III: especificación formal de Historias de Usuario con criterios de aceptación en formato Gherkin (Given-When-Then), Technical Stories de API RESTful, diagrama de Impact Mapping y Product Backlog priorizado por valor de negocio con estimación en Story Points. |
| **0.4.0** | 2026-10-02 | Equipo FuelPoint | Incorporación del Capítulo IV: definición de Style Guidelines, Information Architecture (SEO tags), Wireframes y Mockups en Figma (Desktop y Mobile), User Flows, arquitectura DDD con C4 Model (Context, Container y Componentes), diagramas de clases UML y diseño de base de datos relacional. |
| **1.0.0** | 2026-10-08 | Equipo FuelPoint | **Versión consolidada para la entrega del Trabajo Parcial (TB1 — Stage Review):** Incorporación de la sección 5.2.2 con la documentación del Sprint 2 para la primera versión de la Web Application (Vue 3 / PrimeVue), evidencias de desarrollo en GitFlow, ejecución de vistas, despliegue en producción, actualización de Student Outcome y conclusiones. |
| **1.0.1** | 2026-10-09 | Equipo FuelPoint | Integración completa de los 10 Pull Requests del frontend en develop y main; configuración del pipeline CI/CD en GitHub Actions con 90/90 pruebas unitarias con Vitest y despliegue automático a producción en Firebase Hosting. |
| **1.1.0** | 2026-11-11 | Equipo FuelPoint | **Versión para la entrega AV2:** incorporación de la sección 5.2.3 con la documentación del Sprint 3 (Web Services RESTful en ASP.NET Core .NET 10, Entity Framework Core y MySQL 8, 82/82 pruebas automatizadas y configuración de despliegue en Render); actualización de 5.1 con el repositorio del backend y su configuración de despliegue; guías de Validation Interviews (5.3) y estructura para su registro y evaluación heurística; secciones de videos About-the-Product y About-the-Team (5.4 y 5.5); actualización de Student Outcome, conclusiones y anexos; corrección de la atribución de cuentas en 5.2.2.8. |

---

> **Estado de evidencia TB1 (09/10/2026):** Aplicación web frontend completamente integrada, probada (90/90 pruebas aprobadas en Vitest) y desplegada a producción en Firebase Hosting mediante pipeline automatizado de GitHub Actions. Todos los Bounded Contexts cuentan con Pull Requests integrados y verificados en las ramas `develop` y `main`, documentados en [5.2.2.4](docs/chapter5.md#5224-development-evidence-for-sprint-review), [5.2.2.7](docs/chapter5.md#5227-software-deployment-evidence-for-sprint-review) y [5.2.2.8](docs/chapter5.md#5228-team-collaboration-insights-during-sprint).

> **Estado de evidencia AV2 (11/11/2026):** Los Web Services de los nueve Bounded Contexts están integrados en `main` del repositorio [Full_Tank_Backend](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend) (commit `fde0498`) y superan 82/82 pruebas automatizadas. La API y MySQL se validaron en contenedores locales y su despliegue en Render está configurado, pero **aún no se han publicado**; la Web Application publicada sigue usando la API simulada. Las entrevistas de validación y los videos About-the-Product y About-the-Team están pendientes. Ver [5.2.3](docs/chapter5.md#523-sprint-3), [5.3](docs/chapter5.md#53-validation-interviews), [5.4](docs/chapter5.md#54-video-about-the-product) y [5.5](docs/chapter5.md#55-video-about-the-team).

## Project Report Collaboration Insights

**Repositorio del informe:** [https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Fuel_Point_Document](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Fuel_Point_Document)

El informe de proyecto de FullTank se gestiona de manera colaborativa bajo el formato Markdown en GitHub, aplicando el flujo de trabajo **GitFlow**, **Conventional Commits** y **Semantic Versioning 2.0.0**. La elaboración de la documentación se distribuye entre los miembros del equipo garantizando trazabilidad, revisión por pares (*Pull Requests*) y consistencia con las directivas del enunciado del curso.

### Dinámica de Trabajo y Distribución de Responsabilidades Documentales

Durante el desarrollo de las entregas **AV1**, **TB1** y **AV2**, los cinco integrantes del equipo asumieron la autoría e integración de los capítulos correspondientes mediante ramas de característica específicas (`feat/chapter*`):

1. **Corvacho Damian, Brayan Alexis:**
   - Creación y configuración inicial del repositorio documental `Fuel_Point_Document`.
   - Redacción del Capítulo I: perfil de la startup FuelPoint, perfiles de integrantes, antecedentes del problema (5W2H) y Lean UX Process (Canvas, Problem Statement e hipótesis).
   - Liderazgo técnico en la arquitectura base del Frontend (`feat/shared`), coordinación general de entregas y consolidación del `README.md` raíz.
   - AV2: base compartida e IAM del backend, configuración de producción e integración de las ramas del backend en `main`.
2. **Huingo Tello, Frank Anthony:**
   - Redacción del Capítulo II (Requirements Elicitation & Analysis): diseño de entrevistas a empresas solicitantes y proveedoras, registro de videos en Microsoft Stream, análisis de entrevistas y arquetipos User Persona.
   - Colaboración en el Capítulo V (Sprint 1: Landing Page y Sprint 2: módulo de Fulfillment y Notification).
   - AV2: guías de Validation Interviews (5.3.1) y Web Services de Equipment, Fulfillment y Notification.
3. **Mantilla Maldonado, Enrique Manuel:**
   - Redacción del Capítulo III (Requirements Specification): formulación de Epics y User Stories con criterios de aceptación en sintaxis Gherkin, Technical Stories para la API, Impact Mapping y estructuración del Product Backlog en Trello.
   - Colaboración en el Capítulo V (Sprint 2: módulos de Catalog y Ordering).
   - AV2: Web Services de Catalog, Inventory y Ordering, persistencia con EF Core y MySQL, y configuración de Render.
4. **Payano Puchuri, Joan Fabricio:**
   - Redacción del Capítulo IV (Product Design): guías de estilo visual (*Style Guidelines*), arquitectura de información (SEO y metatags), Wireframes, Mockups y User Flows en Figma para desktop y mobile.
   - Colaboración en el Capítulo V (Sprint 2: módulos de Payment y Reporting).
   - AV2: Web Services de Payment (checkout simulado y comprobantes) y Reporting & Analytics.
5. **Carhuayal Suarez, Joan Salvador:**
   - Redacción del Capítulo IV (Domain-Driven Architecture): modelado de Bounded Contexts en Miro (Design-Level EventStorming), diagramas C4 (Context, Container, Components), diagramas de clases UML y diseño de Base de Datos.
   - Redacción del Capítulo V: documentación del Sprint 1 (Landing Page) y Sprint 2 (Equipment e Inventory).
   - AV2: aporte pendiente de confirmar por el equipo.

### Evidencias de Colaboración en GitHub (Analytics & Commits)

A continuación se presentan las evidencias de participación activa y balanceada de todos los miembros del equipo en la evolución de este repositorio:

#### Gráfico de Contribuciones y Commits por Integrante (`Insights -> Contributors`)
El flujo de trabajo colaborativo y la participación equitativa de los integrantes del equipo se audita directamente en las métricas del repositorio oficial:
- **Enlace a métricas de colaboradores en GitHub:** [GitHub Contributors Graph - Fuel_Point_Document](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Fuel_Point_Document/graphs/contributors)

#### Historial de Ramas y Pull Requests (`Network Graph`)
La trazabilidad del modelo GitFlow mediante ramas de características independientes (`feat/*`), integración continua en `develop` y lanzamientos de versión se audita en el grafo de red oficial:
- **Enlace al grafo de red de GitHub:** [GitHub Network Graph - Fuel_Point_Document](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Fuel_Point_Document/network)

---

## Contenido

- [Student Outcome](#student-outcome)
- [Capítulo I: Introducción](docs/chapter1.md#capítulo-i-introducción)
  - [1.1 Startup Profile](docs/chapter1.md#11-startup-profile)
    - [1.1.1 Descripción de la Startup](docs/chapter1.md#111-descripción-de-la-startup)
    - [1.1.2 Perfiles de integrantes del equipo](docs/chapter1.md#112-perfiles-de-integrantes-del-equipo)
  - [1.2 Solution Profile](docs/chapter1.md#12-solution-profile)
    - [1.2.1 Antecedentes y problemática](docs/chapter1.md#121-antecedentes-y-problemática)
    - [1.2.2 Lean UX Process](docs/chapter1.md#122-lean-ux-process)
      - [1.2.2.1 Lean UX Problem Statements](docs/chapter1.md#1221-lean-ux-problem-statements)
      - [1.2.2.2 Lean UX Assumptions](docs/chapter1.md#1222-lean-ux-assumptions)
      - [1.2.2.3 Lean UX Hypothesis Statements](docs/chapter1.md#1223-lean-ux-hypothesis-statements)
      - [1.2.2.4 Lean UX Canvas](docs/chapter1.md#1224-lean-ux-canvas)
  - [1.3 Segmentos objetivo](docs/chapter1.md#13-segmentos-objetivo)
- [Capítulo II: Requirements Elicitation & Analysis](docs/chapter2.md#capítulo-ii-requirements-elicitation--analysis)
  - [2.1 Competidores](docs/chapter2.md#21-competidores)
    - [2.1.1 Análisis competitivo](docs/chapter2.md#211-análisis-competitivo)
    - [2.1.2 Estrategias y tácticas frente a competidores](docs/chapter2.md#212-estrategias-y-tácticas-frente-a-competidores)
  - [2.2 Entrevistas](docs/chapter2.md#22-entrevistas)
    - [2.2.1 Diseño de entrevistas](docs/chapter2.md#221-diseño-de-entrevistas)
    - [2.2.2 Registro de entrevistas](docs/chapter2.md#222-registro-de-entrevistas)
    - [2.2.3 Análisis de entrevistas](docs/chapter2.md#223-análisis-de-entrevistas)
  - [2.3 Needfinding](docs/chapter2.md#23-needfinding)
    - [2.3.1 User Personas](docs/chapter2.md#231-user-personas)
    - [2.3.2 User Task Matrix](docs/chapter2.md#232-user-task-matrix)
    - [2.3.3 User Journey Mapping](docs/chapter2.md#233-user-journey-mapping)
    - [2.3.4 Empathy Mapping](docs/chapter2.md#234-empathy-mapping)
  - [2.4 Big Picture Event Storming](docs/chapter2.md#24-big-picture-event-storming)
  - [2.5 Ubiquitous Language](docs/chapter2.md#25-ubiquitous-language)
- [Capítulo III: Requirements Specification](docs/chapter3.md#capítulo-iii-requirements-specification)
  - [3.1 User Stories](docs/chapter3.md#31-user-stories)
    - [3.1.1 Historias funcionales](docs/chapter3.md#311-historias-funcionales)
    - [3.1.2 Historias técnicas](docs/chapter3.md#312-historias-técnicas)
  - [3.2 Impact Mapping](docs/chapter3.md#32-impact-mapping)
  - [3.3 Product Backlog](docs/chapter3.md#33-product-backlog)
- [Capítulo IV: Product Design](docs/chapter4.md#capítulo-iv-product-design)
  - [4.1 Style Guidelines](docs/chapter4.md#41-style-guidelines)
    - [4.1.1 General Style Guidelines](docs/chapter4.md#411-general-style-guidelines)
    - [4.1.2 Web Style Guidelines](docs/chapter4.md#412-web-style-guidelines)
  - [4.2 Information Architecture](docs/chapter4.md#42-information-architecture)
    - [4.2.1 Organization Systems](docs/chapter4.md#421-organization-systems)
    - [4.2.2 Labeling Systems](docs/chapter4.md#422-labeling-systems)
    - [4.2.3 SEO Tags and Meta Tags](docs/chapter4.md#423-seo-tags-and-meta-tags)
    - [4.2.4 Searching Systems](docs/chapter4.md#424-searching-systems)
    - [4.2.5 Navigation Systems](docs/chapter4.md#425-navigation-systems)
  - [4.3 Landing Page UI Design](docs/chapter4.md#43-landing-page-ui-design)
    - [4.3.1 Landing Page Wireframe](docs/chapter4.md#431-landing-page-wireframe)
    - [4.3.2 Landing Page Mock-up](docs/chapter4.md#432-landing-page-mock-up)
  - [4.4 Web Applications UX/UI Design](docs/chapter4.md#44-web-applications-uxui-design)
    - [4.4.1 Web Applications Wireframes](docs/chapter4.md#441-web-applications-wireframes)
    - [4.4.2 Web Applications Wireflow Diagrams](docs/chapter4.md#442-web-applications-wireflow-diagrams)
    - [4.4.3 Web Applications Mock-ups](docs/chapter4.md#443-web-applications-mock-ups)
    - [4.4.4 Web Applications User Flow Diagrams](docs/chapter4.md#444-web-applications-user-flow-diagrams)
  - [4.5 Web Applications Prototyping](docs/chapter4.md#45-web-applications-prototyping)
  - [4.6 Domain-Driven Software Architecture](docs/chapter4.md#46-domain-driven-software-architecture)
    - [4.6.1 Design-Level Event Storming](docs/chapter4.md#461-design-level-event-storming)
    - [4.6.2 Software Architecture Context Diagram](docs/chapter4.md#462-software-architecture-context-diagram)
    - [4.6.3 Software Architecture Container Diagrams](docs/chapter4.md#463-software-architecture-container-diagrams)
    - [4.6.4 Software Architecture Components Diagrams](docs/chapter4.md#464-software-architecture-components-diagrams)
  - [4.7 Software Object-Oriented Design](docs/chapter4.md#47-software-object-oriented-design)
    - [4.7.1 Class Diagrams](docs/chapter4.md#471-class-diagrams)
  - [4.8 Database Design](docs/chapter4.md#48-database-design)
    - [4.8.1 Database Diagrams](docs/chapter4.md#481-database-diagrams)
- [Capítulo V: Product Implementation, Validation & Deployment](docs/chapter5.md#capítulo-v-product-implementation-validation--deployment)
  - [5.1 Software Configuration Management](docs/chapter5.md#51-software-configuration-management)
    - [5.1.1 Software Development Environment Configuration](docs/chapter5.md#511-software-development-environment-configuration)
    - [5.1.2 Source Code Management](docs/chapter5.md#512-source-code-management)
    - [5.1.3 Source Code Style Guide & Conventions](docs/chapter5.md#513-source-code-style-guide--conventions)
    - [5.1.4 Software Deployment Configuration](docs/chapter5.md#514-software-deployment-configuration)
  - [5.2 Landing Page, Services & Applications Implementation](docs/chapter5.md#52-landing-page-services--applications-implementation)
    - [5.2.1 Sprint 1](docs/chapter5.md#521-sprint-1)
      - [5.2.1.1 Sprint Planning 1](docs/chapter5.md#5211-sprint-planning-1)
      - [5.2.1.2 Aspect Leaders and Collaborators](docs/chapter5.md#5212-aspect-leaders-and-collaborators)
      - [5.2.1.3 Sprint Backlog 1](docs/chapter5.md#5213-sprint-backlog-1)
      - [5.2.1.4 Development Evidence for Sprint Review](docs/chapter5.md#5214-development-evidence-for-sprint-review)
      - [5.2.1.5 Execution Evidence for Sprint Review](docs/chapter5.md#5215-execution-evidence-for-sprint-review)
      - [5.2.1.6 Services Documentation Evidence for Sprint Review](docs/chapter5.md#5216-services-documentation-evidence-for-sprint-review)
      - [5.2.1.7 Software Deployment Evidence for Sprint Review](docs/chapter5.md#5217-software-deployment-evidence-for-sprint-review)
      - [5.2.1.8 Team Collaboration Insights during Sprint](docs/chapter5.md#5218-team-collaboration-insights-during-sprint)
    - [5.2.2 Sprint 2](docs/chapter5.md#522-sprint-2)
      - [5.2.2.1 Sprint Planning 2](docs/chapter5.md#5221-sprint-planning-2)
      - [5.2.2.2 Aspect Leaders and Collaborators](docs/chapter5.md#5222-aspect-leaders-and-collaborators)
      - [5.2.2.3 Sprint Backlog 2](docs/chapter5.md#5223-sprint-backlog-2)
      - [5.2.2.4 Development Evidence for Sprint Review](docs/chapter5.md#5224-development-evidence-for-sprint-review)
      - [5.2.2.5 Execution Evidence for Sprint Review](docs/chapter5.md#5225-execution-evidence-for-sprint-review)
      - [5.2.2.6 Services Documentation Evidence for Sprint Review](docs/chapter5.md#5226-services-documentation-evidence-for-sprint-review)
      - [5.2.2.7 Software Deployment Evidence for Sprint Review](docs/chapter5.md#5227-software-deployment-evidence-for-sprint-review)
      - [5.2.2.8 Team Collaboration Insights during Sprint](docs/chapter5.md#5228-team-collaboration-insights-during-sprint)
    - [5.2.3 Sprint 3](docs/chapter5.md#523-sprint-3)
      - [5.2.3.1 Sprint Planning 3](docs/chapter5.md#5231-sprint-planning-3)
      - [5.2.3.2 Aspect Leaders and Collaborators](docs/chapter5.md#5232-aspect-leaders-and-collaborators)
      - [5.2.3.3 Sprint Backlog 3](docs/chapter5.md#5233-sprint-backlog-3)
      - [5.2.3.4 Development Evidence for Sprint Review](docs/chapter5.md#5234-development-evidence-for-sprint-review)
      - [5.2.3.5 Execution Evidence for Sprint Review](docs/chapter5.md#5235-execution-evidence-for-sprint-review)
      - [5.2.3.6 Services Documentation Evidence for Sprint Review](docs/chapter5.md#5236-services-documentation-evidence-for-sprint-review)
      - [5.2.3.7 Software Deployment Evidence for Sprint Review](docs/chapter5.md#5237-software-deployment-evidence-for-sprint-review)
      - [5.2.3.8 Team Collaboration Insights during Sprint](docs/chapter5.md#5238-team-collaboration-insights-during-sprint)
  - [5.3 Validation Interviews](docs/chapter5.md#53-validation-interviews)
    - [5.3.1 Diseño de Entrevistas](docs/chapter5.md#531-diseño-de-entrevistas)
    - [5.3.2 Registro de Entrevistas](docs/chapter5.md#532-registro-de-entrevistas)
    - [5.3.3 Evaluaciones según heurísticas](docs/chapter5.md#533-evaluaciones-según-heurísticas)
  - [5.4 Video About-the-Product](docs/chapter5.md#54-video-about-the-product)
  - [5.5 Video About-the-Team](docs/chapter5.md#55-video-about-the-team)
- [Conclusiones](#conclusiones)
- [Bibliografía](#bibliografía)
- [Anexos](#anexos)

---

## Student Outcome

El curso contribuye al cumplimiento del Student Outcome ABET:

**ABET – EAC - Student Outcome 5**  
**Criterio:** La capacidad de funcionar efectivamente en un equipo cuyos miembros juntos proporcionan liderazgo, crean un entorno de colaboración e inclusivo, establecen objetivos, planifican tareas y cumplen objetivos.

El siguiente cuadro recoge las acciones declaradas por los integrantes y sus conclusiones para ABET SO5. La totalidad de diez Bounded Contexts y sus respectivos Pull Requests (#2 al #11) se encuentran integrados y verificados en las ramas `develop` y `main` de la aplicación web, respaldados por la suite de pruebas unitarias con Vitest (90/90 pruebas aprobadas) y el despliegue automático continuo en Firebase Hosting. Para AV2, las acciones se contrastaron con los commits integrados en `main` del repositorio `Full_Tank_Backend` (85 commits, consulta del 11/11/2026).

| Criterio específico | Acciones realizadas | Conclusiones |
|---|---|---|
| **Trabaja en equipo para proporcionar liderazgo en forma conjunta.** | **Corvacho Damian, Brayan Alexis**<br>• **AV1:** Lideró la formulación del Solution Profile, antecedentes (5W2H) y la estrategia de Lean UX. Coordinó la configuración inicial de los repositorios en la organización de GitHub.<br>• **TB1:** Lideró la arquitectura técnica del frontend (`feat/shared`), estandarizando la modularización por Bounded Contexts en Vue 3 y consolidando la integración del módulo de autenticación y gestión de sesiones (`feat/iam`, PR #3 integrado en `develop` y `main`).<br>• **AV2:** Lideró la base compartida y el Bounded Context IAM de los Web Services (BCrypt, JWT y registro vinculado a empresa mediante `registrationToken`) e integró las 19 ramas del backend en `integration/backend` y `main` (release `fde0498`). [Video de Sustentación Individual ABET SO5](https://upcedupe-my.sharepoint.com/:v:/g/personal/u20231a257_upc_edu_pe/IQBpJTQmQ-GCSLqgcJMMXiKDAdbkbObBQoDbAiynOSheS8E?e=mgfoOP&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D).<br><br>**Huingo Tello, Frank Anthony**<br>• **AV1:** Lideró el diseño de entrevistas cualitativas para empresas solicitantes y proveedoras, y gestionó la consolidación de grabaciones de video en Microsoft Stream.<br>• **TB1:** Asumió el liderazgo del Bounded Context de Fulfillment y Logística (`feat/fulfillment`, PR #4) y del módulo de Notificaciones (`feat/notification`, PR #5), definiendo la estructura de despacho de combustible.<br>• **AV2:** Lideró los Web Services de Equipment, Fulfillment y Notification, y diseñó las guías de entrevistas de validación para ambos segmentos (5.3.1).<br><br>**Payano Puchuri, Joan Fabricio**<br>• **AV1:** Lideró el diseño del sistema visual (*Style Guidelines*) en Figma, definiendo paleta cromática, tipografía y lineamientos de accesibilidad WCAG.<br>• **TB1:** Lideró el diseño e implementación del Bounded Context de Pagos (`feat/payment`, PR #10) y de Reportería Operativa (`feat/reporting`, PR #11), estructurando la carga de comprobantes y métricas.<br>• **AV2:** Lideró los Web Services de Payment (checkout simulado atómico con cálculo de IGV y comprobantes académicos) y de Reporting & Analytics.<br><br>**Mantilla Maldonado, Enrique Manuel**<br>• **AV1:** Lideró el levantamiento y refinamiento de Historias de Usuario con sintaxis Gherkin y la priorización del Product Backlog en Trello según valor de negocio.<br>• **TB1:** Lideró la implementación de los módulos de Catálogo (`feat/catalog`, PR #8) y Gestión de Órdenes (`feat/ordering`, PR #9), coordinando el flujo de estados transaccionales.<br>• **AV2:** Lideró los Web Services de Catalog, Inventory y Ordering (aprobación, despacho, recepción y cancelación), la persistencia con Entity Framework Core y MySQL, y la conexión de la API con MySQL privado en Render.<br><br>**Carhuayal Suarez, Joan Salvador**<br>• **AV1:** Lideró el modelado arquitectónico con Domain-Driven Design (Big Picture EventStorming, Bounded Contexts y diagramas C4 Context y Container).<br>• **TB1:** Lideró la implementación del Bounded Context de Inventario (`feat/inventory`, PR #7) y Equipos (`feat/equipment`, PR #6), consolidando las evidencias de desarrollo del Sprint 2.<br>• **AV2:** *Pendiente de confirmar por el equipo.* | **Conclusiones AV1:**<br>El equipo demostró un liderazgo compartido y horizontal al distribuir la responsabilidad de los diversos frentes del proyecto (investigación de usuarios, diseño UX/UI, modelado arquitectónico y desarrollo web). Esta estructura permitió que las decisiones técnicas se tomaran por consenso fundamentado, logrando culminar con éxito la primera versión funcional y desplegada de la Landing Page.<br><br>**Conclusiones TB1:**<br>Para la entrega del Trabajo Parcial, el liderazgo se consolidó a través del modelo de *Aspect Leaders* por Bounded Context. Cada integrante asumió la titularidad técnica sobre su módulo asignado en la Web Application, defendiendo sus pull requests, aplicando revisiones de código estrictas y coordinando las dependencias intermodulares sin depender de una única figura centralizada.<br><br>**Conclusiones AV2:**<br>En el Sprint 3 se mantuvo el liderazgo por Bounded Context: cada integrante con código en el backend conservó los dominios que lideró en el frontend, y Equipment e Inventory se redistribuyeron entre Frank Huingo y Enrique Mantilla. Esto facilitó trasladar los contratos de la Web Application a la API. La integración, en cambio, se concentró en un solo integrante y se realizó sin Pull Requests, por lo que no quedó evidencia de revisión cruzada; el equipo se compromete a retomar los Pull Requests con revisión en el Sprint 4. |
| **Crea un entorno colaborativo e inclusivo, establece metas, planifica tareas y cumple objetivos.** | **Corvacho Damian, Brayan Alexis**<br>• **AV1:** Estableció las convenciones de GitFlow y Conventional Commits, y facilitó las reuniones de retrospectiva en Google Meet.<br>• **TB1:** Diseñó el plan de integración por ramas para evitar colisiones de código, implementó 41 pruebas unitarias en `iam.store.spec.js` y mantuvo el build continuo de la aplicación.<br>• **AV2:** Escribió las pruebas de registro IAM, de acceso entre empresas y de configuración insegura en producción, y validó la configuración de producción y el health check de MySQL.<br><br>**Huingo Tello, Frank Anthony**<br>• **AV1:** Colaboró en la maquetación HTML/CSS de la sección Testimonios de la Landing Page y documentó los resúmenes de entrevistas de Needfinding.<br>• **TB1:** Implementó las vistas de asignación de choferes y cisternas, ejecutó pruebas de interfaz de usuario y colaboró en el cumplimiento de las tarjetas del Sprint Backlog 2.<br>• **AV2:** Escribió las pruebas de reglas de dominio y conversión de unidades y publicó la API en una imagen Docker .NET.<br><br>**Payano Puchuri, Joan Fabricio**<br>• **AV1:** Desarrolló los componentes gráficos de la sección Planes y Precios de la Landing Page y colaboró en la creación de los Empathy Maps.<br>• **TB1:** Desarrolló las pruebas de stores y selectores de pagos (`payment.store.spec.js`), integró componentes de gráficos con PrimeVue y verificó la adaptabilidad responsive.<br>• **AV2:** Escribió las pruebas de totales del checkout y de los datos del comprobante.<br><br>**Mantilla Maldonado, Enrique Manuel**<br>• **AV1:** Implementó las secciones Home y How It Works de la Landing Page, asegurando la consistencia semántica del contenido.<br>• **TB1:** Desarrolló las vistas de creación de solicitudes y detalle de órdenes, colaborando en la sincronización de estados con el resto del equipo en los daily meetings.<br>• **AV2:** Escribió las pruebas del flujo de aprobación, despacho y recepción, y versionó el esquema de MySQL con migraciones de Entity Framework Core.<br><br>**Carhuayal Suarez, Joan Salvador**<br>• **AV1:** Diseñó el diagrama Entidad-Relación relacional y colaboró en el selector de idiomas i18n de la Landing Page.<br>• **TB1:** Implementó las vistas de monitoreo de capacidad de tanques, desarrolló las pruebas de inventario (`inventory.store.spec.js`) y documentó la configuración de despliegue.<br>• **AV2:** *Pendiente de confirmar por el equipo.* | **Conclusiones AV1:**<br>Se fomentó un ambiente de trabajo transparente e inclusivo mediante canales sincrónicos (Google Meet) y asincrónicos (WhatsApp, Trello), donde todos los integrantes aportaron activamente en la definición de metas. Se cumplió el 100% de los compromisos adquiridos en el Sprint 1 dentro de los plazos establecidos.<br><br>**Conclusiones TB1:**<br>El entorno colaborativo maduró significativamente durante el Sprint 2 mediante la integración gradual de 9 Bounded Contexts sobre una base común limpia. La adopción de Pull Requests formales con revisión por pares aseguró que ningún integrante publicara código sin validación cruzada. El cumplimiento riguroso del Sprint Backlog 2 permitió desplegar la primera versión de la Web Application con altos estándares de calidad.<br><br>**Conclusiones AV2:**<br>El Sprint 3 se planificó sobre las 27 historias técnicas de la API (64 SP) y priorizó el MVP antes de IAM. Al cierre, 17 historias están completas, 7 parciales y 3 pendientes, y la API supera 82/82 pruebas automatizadas. Las metas que dependen de todo el equipo (despliegue público, integración con la Web Application y entrevistas de validación) siguen abiertas, y el aporte de uno de los integrantes al backend debe hacerse visible; ambos puntos se incorporan como compromisos del Sprint 4. |

---

## Conclusiones

1. **Validación del Modelo de Negocio y Lean UX:** La investigación cualitativa con empresas solicitantes y proveedoras de combustible confirmó que la fragmentación en la gestión de pedidos (llamadas telefónicas, WhatsApp y hojas de cálculo desconectadas) es la principal causa de desorganización y retrasos en las entregas. La plataforma FullTank demuestra ser una solución viable y pertinente para centralizar las operaciones, brindando trazabilidad en tiempo real a ambos segmentos.
2. **Efectividad de la Arquitectura DDD y Modularidad Frontend:** La descomposición del sistema en 9 Bounded Contexts independientes (IAM, Catalog, Equipment, Inventory, Ordering, Payment, Fulfillment, Notification y Reporting) permitió una distribución eficiente del trabajo durante el Sprint 2. Cada módulo en Vue 3 encapsula su dominio, lógica de aplicación e infraestructura. La aplicación publicada permite operar a ambos segmentos; la totalidad de los 10 Pull Requests se encuentran integrados satisfactoriamente en el repositorio oficial.
3. **Calidad de Software y Buenas Prácticas de Ingeniería:** La aplicación web integrada superó exitosamente 90/90 pruebas automatizadas con Vitest en catorce archivos de especificación (100% de aprobación). Se configuró un pipeline de CI/CD automatizado en GitHub Actions que ejecuta las pruebas, genera la compilación de producción optimizada y despliega continuamente en Firebase Hosting ante cada push a las ramas `develop` y `main`, publicado oficialmente bajo el tag de release `v1.0.0`.
4. **Web Services y persistencia (AV2):** Los nueve Bounded Contexts cuentan con Web Services RESTful en ASP.NET Core (.NET 10) con persistencia en MySQL mediante Entity Framework Core, documentados con OpenAPI / Swagger y respaldados por 82/82 pruebas automatizadas. La API aplica en el servidor las reglas críticas del negocio: precios tomados del inventario, reserva y descuento de stock, transiciones de estado de las órdenes, cálculo del IGV y control de acceso por empresa. Al cierre de esta versión, la API está validada en contenedores locales y preparada para Render, pero su despliegue público y la conexión con la Web Application siguen pendientes.
5. **Recomendaciones y Roadmap hacia el Trabajo Final (TB2):**
   - **Cierre de AV2:** Publicar la API y MySQL en Render, conectar la Web Application con la API pública y realizar las entrevistas de validación (3 a 5 por segmento) con su evaluación heurística.
   - **Fase TB2 (Sprint 4):** Completar la recuperación de contraseña, el cierre de sesión, la exportación de reportes en PDF y las operaciones de eliminación pendientes; reconciliar los criterios de aceptación del flujo de pagos con la simulación implementada; integrar mediante Pull Requests con revisión, e incorporar a la nueva versión de los artefactos los hallazgos de las entrevistas de validación.

---

## Bibliografía

- Conventional Commits. (2020). *Conventional Commits 1.0.0: A specification for adding human and machine readable meaning to commit messages*. https://www.conventionalcommits.org/
- Driessen, V. (2010). *A successful Git branching model*. nvie.com. https://nvie.com/posts/a-successful-git-branching-model/
- Evans, E. (2003). *Domain-Driven Design: Tackling Complexity in the Heart of Software*. Addison-Wesley Professional.
- Gothelf, J., & Seiden, J. (2021). *Lean UX: Designing Great Products with Agile Teams* (3rd ed.). O'Reilly Media.
- Instituto Nacional de Estadística e Informática. (2025). *Demografía Empresarial en el Perú: III trimestre de 2025*. https://www.inei.gob.pe/media/MenuRecursivo/boletines/boletin_demografia_iiit25.pdf
- Microsoft. (2024). *ASP.NET Core Documentation: Build modern, fast, and scalable web apps and APIs*. https://learn.microsoft.com/en-us/aspnet/core/
- Microsoft. (2025). *Entity Framework Core documentation*. https://learn.microsoft.com/en-us/ef/core/
- Nielsen, J. (1994). *10 Usability Heuristics for User Interface Design*. Nielsen Norman Group. https://www.nngroup.com/articles/ten-usability-heuristics/
- Render. (2026). *Blueprint YAML Reference*. https://render.com/docs/blueprint-spec
- Organismo Supervisor de la Inversión en Energía y Minería. (2024). *Resolución de Consejo Directivo N.° 150-2024-OS/CD: Reglamento del Registro de Hidrocarburos*. https://www.osinergmin.gob.pe/seccion/centro_documental/hidrocarburos/RegistroHidrocarburo/Registro-Hidrocarburos/Osinergmin-150-2024-OS-CD-Reglamento.pdf
- Organismo Supervisor de la Inversión en Energía y Minería. (2025). *Demanda nacional de combustibles líquidos por departamento, diciembre de 2025*. https://www.osinergmin.gob.pe/seccion/centro_documental/hidrocarburos/SCOP/SCOP-DOCS/2025/01-Demanda-Nacional-Combustibles-Liquidos-Diciembre-2025.pdf
- PrimeTek Informatics. (2024). *PrimeVue: The Next-Gen UI Component Suite for Vue.js*. https://primevue.org/
- Schwaber, K., & Sutherland, J. (2020). *The Scrum Guide: The Definitive Guide to Scrum: The Rules of the Game*. Scrum.org. https://scrumguides.org/
- Semantic Versioning. (2020). *Semantic Versioning 2.0.0*. https://semver.org/
- Vue.js Team. (2024). *Vue.js: The Progressive JavaScript Framework*. https://vuejs.org/
- World Wide Web Consortium (W3C). (2023). *Web Content Accessibility Guidelines (WCAG) 2.1*. https://www.w3.org/TR/WCAG21/

---

## Anexos

### Anexo A - Videos de Exposiciones

| Entrega | Título del Video | Plataforma | Enlace de Visualización | Duración |
|---|---|---|---|:---:|
| **AV1** | Exposición de Avance 1 — Presentación de Proyecto y Landing Page | YouTube | [Ver Video en YouTube](https://youtu.be/slU0pE19KAY) | 21:27 |
| **TB1** | Exposición de Trabajo Parcial — Sustentación ABET SO5 y Frontend Web Application | Microsoft Stream | [Ver exposición TB1 en Microsoft Stream](https://upcedupe-my.sharepoint.com/:v:/g/personal/u20231a257_upc_edu_pe/IQBOLr6orh8kSYVocJuNA4awAZE_KVDNpkV2wqSCSsXiDLU?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D&e=7koIIx) | 21:39 |

| **AV2** | Exposición de Avance 2 — Web Services, integración y validación | Pendiente | *Pendiente de publicación* | — |
| **AV2** | About-the-Product (1–3 minutos) | Pendiente | *Pendiente de publicación* ([5.4](docs/chapter5.md#54-video-about-the-product)) | — |
| **AV2** | About-the-Team | Pendiente | *Pendiente de publicación* ([5.5](docs/chapter5.md#55-video-about-the-team)) | — |

> *Nota: El video de exposición de AV1 cuenta con acceso público en YouTube, mientras que el enlace de TB1 en Microsoft Stream se encuentra restringido a la organización institucional UPC.*

### Anexo B - Repositorios Oficiales y Artefactos Digitales

| Artefacto / Producto | Propósito | Enlace Oficial |
|---|---|---|
| **Project Report Repository** | Repositorio de documentación oficial en Markdown | [Fuel_Point_Document en GitHub](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Fuel_Point_Document) |
| **Landing Page Repository** | Código fuente de la página de aterrizaje (HTML5/CSS3/JS) | [Full_Tank_Landing_Page en GitHub](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Landing_Page) |
| **Landing Page Deployed** | Despliegue público en producción de la Landing Page | [FullTank Landing Page en GitHub Pages](https://1asi0730-2620-16129-g1-fuelpoint.github.io/Full_Tank_Landing_Page/) |
| **Web Application Repository** | Código fuente del Frontend SPA (Vue 3, Pinia, PrimeVue) | [Full_Tank_Frontend en GitHub](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Frontend) |
| **Web Application Deployed** | Frontend publicado en Firebase Hosting; demo académica TB1 | [FullTank Web App en Producción](https://full-tank-964e2.web.app/) |
| **Web Services Repository** | Código fuente de la API RESTful (ASP.NET Core .NET 10, EF Core, MySQL) | [Full_Tank_Backend en GitHub](https://github.com/1ASI0730-2620-16129-G1-FuelPoint/Full_Tank_Backend) |
| **Web Services Deployed** | API y documentación Swagger publicadas en Render | *Pendiente de publicación* ([5.2.3.7](docs/chapter5.md#5237-software-deployment-evidence-for-sprint-review)) |
| **Tablero del Proyecto (Trello)** | Tableros Kanban de Product Backlog y Sprints | [Tablero Oficial FullTank en Trello](https://trello.com/b/6h5mZ8L6) |
| **Diseño y Prototipo (Figma)** | Wireframes, Mockups y Prototipo Navegable | [FullTank en Figma](https://www.figma.com/design/ZMHB35H60u2eUhctevkVKc/Fullank-Completo?node-id=0-1) |
| **Sesión DDD EventStorming (Miro)** | Lienzo de modelado de Bounded Contexts y eventos | [EventStorming FullTank en Miro](https://miro.com/app/board/uXjVGgOzeI4=/) |

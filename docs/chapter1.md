# Capítulo I: Introducción

## 1.1 Startup Profile

### 1.1.1 Descripción de la Startup

**FuelPoint** es una startup peruana orientada a la transformación digital del abastecimiento corporativo de combustible. Su propósito es conectar a empresas que necesitan combustible para mantener sus operaciones con empresas autorizadas para comercializarlo y distribuirlo, reduciendo la fragmentación de información que aparece cuando una operación se coordina mediante llamadas, correos, mensajería instantánea y hojas de cálculo separadas.

FuelPoint desarrolla **FullTank**, una solución web B2B que centraliza las solicitudes, su evaluación, la coordinación logística, el seguimiento de estados y el historial de las operaciones. El producto conserva la idea de negocio planteada originalmente, pero se implementará en un nuevo entorno de aplicación web distribuida: una Landing Page pública, una Web Application responsive integrada con un RESTful API propio y un servicio externo de terceros. La experiencia estará disponible desde navegadores de escritorio y dispositivos móviles, tendrá inglés como idioma predeterminado y ofrecerá español latinoamericano como idioma alternativo.

**Misión.** Facilitar operaciones de abastecimiento de combustible más ordenadas, transparentes y verificables mediante una solución web que conecte a compradores y proveedores, reduzca los errores de coordinación y permita tomar decisiones con información centralizada.

**Visión.** Ser una startup de referencia en Latinoamérica para la digitalización del abastecimiento corporativo de combustible, reconocida por la confiabilidad, accesibilidad y trazabilidad de sus productos digitales.

**Principios de trabajo.**

- **Trazabilidad:** cada cambio relevante de una solicitud debe poder identificarse y consultarse.
- **Confiabilidad:** la información presentada debe ser consistente y útil para coordinar operaciones reales.
- **Accesibilidad:** las experiencias deben poder ser percibidas, comprendidas y operadas por la mayor cantidad posible de usuarios.
- **Transparencia:** compradores y proveedores deben conocer el estado, los responsables y las condiciones relevantes de una operación.
- **Mejora continua:** las decisiones del producto se revisarán con evidencia obtenida de los segmentos objetivo.

### 1.1.2 Perfiles de integrantes del equipo

| Foto | Apellidos y nombres | Código | Carrera | Perfil y habilidades |
|---|---|---|---|---|
| <img src="../assets/chapter1/Integrantes/Brayan.png" alt="Brayan Alexis Corvacho Damian" width="80"> | Brayan Alexis Corvacho Damian | U20231a257 | Ingeniería de Software | Estudiante de Ingeniería de Software en la UPC. Poseo conocimientos sólidos en Python, JavaScript y desarrollo web. Me apasiona la resolución de problemas algorítmicos y el trabajo en equipo para crear soluciones innovadoras. |
| <img src="../assets/chapter1/Integrantes/Frank.jpg" alt="Frank Anthony Huingo Tello" width="80"> | Frank Anthony Huingo Tello | U202319057 | Ingeniería de Software | Estudiante de Ingeniería de Software en la UPC. Poseo conocimientos sólidos en HTML, CSS y JavaScript. Me apasiona aprender cosas nuevas y aplicarlas en el desarrollo de mis cursos de carrera.|
| <img src="../assets/chapter1/Integrantes/JoanFT.png" alt="Joan Fabricio Payano Puchuri" width="80"> | Joan Fabricio Payano Puchuri | U202318620 | Ingeniería de Software | Estudiante de Ingeniería de Software en la UPC, con sólidos conocimientos en C++, Python, JavaScript, HTML y CSS. Me apasiona el desarrollo de software y la búsqueda constante de nuevas formas de mejorar mis habilidades. Destaco por mi capacidad para trabajar en equipo, asumir nuevos retos y adaptarme a diferentes situaciones, siempre con la disposición de aprender, aportar soluciones y dar lo mejor de mí en cada proyecto.|
| <img src="../assets/chapter1/Integrantes/Enrique.jpg" alt="Enrique Manuel Mantilla Maldonado" width="80"> | Enrique Manuel Mantilla Maldonado | U20231B842 | Ingeniería de Software | Estudiante de Ingeniería de Software en la UPC, con sólidos conocimientos en Python, C++ y JavaScript. Me apasiona la tecnología y el desarrollo de software, y busco aprender cosas nuevas en el camino.|
| <img src="../assets/chapter1/Integrantes/JoanCS.jpeg" alt="Joan Salvador Carhuayal Suarez" width="80"> | Joan Salvador Carhuayal Suarez | U202219040 | Ingeniería de Software | Estudiante de Ingeniería de Software en la UPC, tengo conocimientos en los lenguajes de programación de Python, C++, HTLM, CSS y JavaScript. Me gusta el mundo de la tecnología y el desarrollo de software, espero seguir mejorando mis habilidades y conocimientos para formarme como profesional.|

## 1.2 Solution Profile

### 1.2.1 Antecedentes y problemática

- **What? (¿Qué?)**  
  La problemática principal es la falta de un sistema centralizado y digital para gestionar los pedidos de combustible, lo que genera errores humanos, duplicación de esfuerzos y retrasos en las entregas.

- **When? (¿Cuándo?)**  
  El problema se presenta constantemente en el proceso de gestión de pedidos, especialmente cuando hay un alto volumen de solicitudes o múltiples pedidos a coordinar.

- **Where? (¿Dónde?)**  
  El problema ocurre en empresas solicitantes de combustible y proveedores, tanto en áreas urbanas como rurales, donde la infraestructura digital aún no está optimizada.

- **Who? (¿Quién?)**  
  Los principales afectados son las empresas solicitantes (medianas y grandes), los proveedores de combustible y los encargados de la logística y gestión de pedidos.

- **Why? (¿Por qué?)**  
  El problema radica en la falta de integración entre los métodos actuales de gestión (como correos y aplicaciones de mensajería), que dificultan un control centralizado y preciso de los pedidos.

- **How? (¿Cómo?)**  
  Los procesos actuales son desorganizados, utilizando diversas plataformas desconectadas, lo que impide tener un flujo de trabajo eficiente y controlado.

- **How Much? (¿Cuánto?)**  
  La magnitud del problema es considerable, pues cada día se pierden horas valiosas debido a la ineficiencia y los errores, lo que incrementa los costos operativos y puede generar pérdidas económicas significativas.

### 1.2.2 Lean UX Process

FuelPoint aplica Lean UX al desarrollo de FullTank para convertir las creencias iniciales del equipo en hipótesis que se puedan comprobar. El punto de partida es el Lean UX Canvas de la sección 1.2.2.4, que organiza en un solo tablero el problema de negocio, los usuarios, las soluciones propuestas, los resultados esperados y lo que el equipo necesita aprender primero. Las secciones siguientes desarrollan cada una de esas ideas.

Las assumptions de esta sección no son hechos confirmados. Se validarán mediante las entrevistas de Needfinding, los artefactos de UX, los prototipos y la evidencia de uso del producto. Si la evidencia no las respalda, se ajustarán antes de comprometer esfuerzo de desarrollo.

#### 1.2.2.1 Lean UX Problem Statements

El Problem Statement sintetiza el problema de negocio identificado en el Lean UX Canvas. Siguiendo rigurosamente las directrices del enunciado oficial y la metodología de Gothelf y Seiden (2021), **se elabora un único Problem Statement para todo el proyecto**, considerando de manera articulada a ambos segmentos objetivo (empresas solicitantes y empresas proveedoras de combustible) bajo la plantilla de *Brand new initiative*.

**Plantilla oficial de Lean UX (*Brand new initiative*):**

> *The current state of [the domain we are working in] has focused mainly on [these customer segments, these pain points, these workflows, etc.].*  
> *What existing products/services fail to address is [this gap or change in the marketplace].*  
> *Our product/service will address this gap by [this product strategy or approach].*  
> *Our initial focus will be [this audience segment].*  
> *We’ll know we are successful when we see [these measurable behaviors in our target audience].*  

**Problem Statement de FullTank (Versión en inglés):**

> **The current state of** commercial and industrial B2B fuel distribution **has focused mainly on** corporate requesters (construction, mining, logistics) and licensed fuel suppliers managing orders through informal, fragmented channels such as phone calls, emails, messaging apps, and disconnected spreadsheets. These manual workflows result in severe operational disorganization, high transcription error rates, delivery delays, and a total lack of real-time supply chain visibility.  
> **What existing products/services fail to address is** an integrated, collaborative digital B2B platform that structures the entire order-to-delivery lifecycle—including demand specification, inventory availability, multi-step order approvals, payment receipt validation, and fleet dispatch coordination—without requiring expensive specialized proprietary telemetry hardware.  
> **Our product/service will address this gap by** providing FullTank, a centralized responsive web application featuring real-time order tracking, automated domain event notifications, clear status synchronization, digital voucher verification, and fleet assignment workflows tailored to corporate operations.  
> **Our initial focus will be** medium and large industrial requesting companies with intensive machinery operations and regional licensed fuel distribution suppliers in the Lima and Callao metropolitan areas.  
> **We’ll know we are successful when we see** that over 70% of placed fuel orders are fulfilled and closed without requiring post-placement manual corrections, customer follow-up calls decrease by at least 30%, and active suppliers achieve a monthly platform retention rate greater than 80%.

**Problem Statement de FullTank (Traducción en español):**

> **El estado actual de** la distribución comercial e industrial de combustible B2B **se ha enfocado principalmente en** empresas solicitantes corporativas (construcción, minería, logística) y proveedores de combustible autorizados que gestionan sus pedidos mediante canales informales y fragmentados como llamadas telefónicas, correos electrónicos, mensajería instantánea y hojas de cálculo desconectadas. Estos flujos de trabajo manuales provocan desorganización operativa, altos índices de error al transcribir datos, demoras en el abastecimiento y una falta absoluta de trazabilidad en tiempo real de la cadena de suministro.  
> **Lo que los productos y servicios existentes no resuelven es** una plataforma web B2B colaborativa e integrada que estructure todo el ciclo de vida del pedido (desde la solicitud de abastecimiento y consulta de inventario, hasta la aprobación de órdenes, validación de comprobantes de pago y asignación de flotas de despacho) sin depender de costosos sistemas de hardware propietario.  
> **Nuestro producto abordará esta brecha mediante** FullTank, una aplicación web responsive centralizada con seguimiento de pedidos en tiempo real, notificaciones automáticas ante eventos de dominio, sincronización de estados compartidos, validación digital de comprobantes y coordinación logística de cisternas adaptada a operaciones corporativas.  
> **Nuestro enfoque inicial serán** las empresas solicitantes medianas y grandes con alto consumo de combustible para maquinaria pesada y los distribuidores regionales autorizados de combustible en Lima y Callao.  
> **Sabremos que tenemos éxito cuando observemos que** más del 70 % de los pedidos de combustible se completan y cierran sin necesidad de correcciones manuales posteriores, las llamadas telefónicas de seguimiento se reduzcan en al menos un 30 %, y los proveedores activos mantengan una retención mensual superior al 80 % dentro de la plataforma.

#### 1.2.2.2 Lean UX Assumptions

Las assumptions se organizan en cinco categorías que corresponden a los recuadros del Lean UX Canvas. Cada categoría desarrolla las ideas registradas en el recuadro correspondiente.

**Business Assumptions** 

- El sector de distribución de combustibles tiene serias ineficiencias porque la gestión de pedidos depende de llamadas telefónicas, correos electrónicos y aplicaciones de mensajería.
- Esa informalidad es la causa de la desorganización, de los errores y de la falta de visibilidad en tiempo real que sufren solicitantes y proveedores.
- Estos problemas afectan directamente la eficiencia operativa de las empresas y la relación entre proveedores y clientes, por lo que ambos segmentos tienen motivos para cambiar su forma de trabajar.
- Los usuarios valoran la comunicación directa y las notificaciones en tiempo real como la forma más efectiva de reducir los errores en las entregas. Este es el supuesto más importante de validar primero: si resulta falso, la solución principal perdería sentido y habría que replantear el enfoque del producto.

**Business Outcome Assumptions** 

- Los usuarios usan FullTank de manera recurrente para mejorar la trazabilidad de sus pedidos en tiempo real.
- Los usuarios se mantienen activos de forma regular en la plataforma, lo que se medirá con la **tasa de retención mensual**.
- Los envíos se completan sin necesidad de correcciones posteriores, lo que se medirá con el **porcentaje de envíos completados sin correcciones**.
- Los usuarios crean pedidos, registran pagos y gestionan transportistas dentro de la plataforma cada semana, lo que se medirá con el **número promedio de interacciones por semana**.

**User Assumptions** 

- **Empresas solicitantes de combustible:** son empresas medianas y grandes que necesitan combustible de forma constante para desarrollar sus operaciones. Lo usan para alimentar maquinaria, vehículos o equipos, por lo que un retraso en el abastecimiento puede detener su trabajo. Buscan procesos más ágiles, ordenados y confiables para gestionar sus pedidos.
- **Proveedores de combustible:** son empresas dedicadas a la distribución de combustibles que atienden principalmente a clientes corporativos o industriales. Coordinan varios pedidos, transportistas y entregas al mismo tiempo. Buscan herramientas que les permitan optimizar sus operaciones y diferenciarse en un mercado cada vez más competitivo.

**User Outcome and Benefit Assumptions** 

Empresas solicitantes de combustible:

- Asegurar el abastecimiento oportuno de combustible para que su maquinaria y sus operaciones no se detengan.
- Reducir los errores que provoca la informalidad de los procesos actuales, como pedidos mal registrados o datos incompletos.
- Mantener una comunicación constante con sus proveedores y saber en qué estado está cada pedido sin tener que llamar.

Proveedores de combustible:

- Mejorar la experiencia de sus clientes mediante canales digitales que reemplacen las llamadas y los mensajes dispersos.
- Reducir los errores en las entregas causados por información incompleta o mal gestionada.
- Optimizar la planificación logística y la distribución de sus pedidos.

**Feature Assumptions** 

1. Una **aplicación web de trazabilidad en tiempo real** permitirá a solicitantes y proveedores visualizar el estado de cada pedido de combustible en cualquier etapa del ciclo de vida.
2. Las **alertas y notificaciones automáticas en la web** sobre eventos críticos (creación, aprobación, despacho y entrega) reducirán la incertidumbre y eliminarán las llamadas de seguimiento manual.
3. Un **dashboard interactivo con métricas clave y KPIs operativos** (pedidos completados, tiempos de entrega y volumen despachado) permitirá a los usuarios supervisar su rendimiento logístico.
4. Un **módulo de registro y verificación de comprobantes de pago** permitirá asociar transferencias bancarias a las órdenes, agilizando la validación financiera previa al despacho.
5. Un **módulo de gestión y asignación de recursos logísticos (flota y conductores)** permitirá a los distribuidores organizar sus cisternas disponibles y supervisar la entrega física.
6. El **historial transaccional y los reportes descargables (PDF)** darán a clientes y proveedores un registro formal y auditable de sus consumos y ventas acumuladas.

#### 1.2.2.3 Lean UX Hypothesis Statements

Conforme a las especificaciones del enunciado, se formula un **Hypothesis Statement por cada una de las seis Feature Assumptions** definidas previamente, empleando la plantilla estándar de 4 cláusulas de Lean UX (Gothelf & Seiden, 2021):

> *We believe we will achieve [this business outcome]*  
> *If [these personas]*  
> *Attain [this benefit/user outcome]*  
> *With [this feature or solution]*  

---

**Hypothesis Statement 01 (Trazabilidad en tiempo real):**
- **We believe we will achieve** an increase of over 70% in orders completed without operational incidents and a monthly platform retention rate exceeding 80%
- **If** corporate logistics managers (such as Carlos Ramírez) and fuel distribution coordinators (such as Andrea López)
- **Attain** immediate visibility and transparency regarding the real-time stage of fuel requests from creation to delivery
- **With** a responsive web application for real-time order lifecycle tracking with synchronized multi-stage statuses.

*(Traducción: Creemos que alcanzaremos más de un 70 % de pedidos completados sin incidencias y una retención mensual superior al 80 % si los gestores logísticos solicitantes y coordinadores proveedores obtienen visibilidad y transparencia inmediata del estado de sus pedidos en tiempo real con una aplicación web responsive de seguimiento de pedidos).*

---

**Hypothesis Statement 02 (Alertas y notificaciones automáticas):**
- **We believe we will achieve** a 30% reduction in customer follow-up phone calls and messaging inquiries
- **If** requesting operations managers and customer support coordinators
- **Attain** timely and automated awareness of critical order lifecycle events (approvals, dispatch departures, and delivery confirmations)
- **With** an in-app and web alert notification module triggered by domain state changes.

*(Traducción: Creemos que lograremos reducir en un 30 % las llamadas y mensajes de seguimiento si los encargados de operaciones y atención al cliente obtienen información oportuna de eventos críticos del pedido con un módulo de notificaciones y alertas automáticas en la web).*

---

**Hypothesis Statement 03 (Dashboard con métricas y KPIs):**
- **We believe we will achieve** a 25% increase in operational planning efficiency and decision-making speed for registered supplier companies
- **If** fuel supplier sales and operations managers
- **Attain** consolidated visibility of daily active orders, total volume dispatched, and customer fulfillment performance metrics
- **With** an interactive operational dashboard featuring real-time KPIs and trend charts.

*(Traducción: Creemos que lograremos un incremento del 25 % en la eficiencia de planificación operativa de los proveedores si sus gerentes comerciales y operativos obtienen una visión consolidada de órdenes activas y volumen despachado con un dashboard interactivo de métricas operativas).*

---

**Hypothesis Statement 04 (Registro y validación de pagos):**
- **We believe we will achieve** a 40% reduction in order processing lead time prior to logistics dispatch
- **If** corporate purchasers and supplier billing analysts
- **Attain** secure, verifiable upload and quick approval of payment vouchers directly associated with specific fuel orders
- **With** a dedicated digital payment voucher registration and verification module.

*(Traducción: Creemos que lograremos una reducción del 40 % en el tiempo de procesamiento de pedidos previo al despacho si los compradores corporativos y analistas de facturación obtienen una validación rápida y verificable de comprobantes de pago con un módulo digital de registro y verificación de comprobantes).*

---

**Hypothesis Statement 05 (Gestión de flota y transportistas):**
- **We believe we will achieve** a 20% reduction in fuel delivery transit delays and route assignment conflicts
- **If** distribution logistics coordinators
- **Attain** structured control over tanker vehicle availability, driver licensing validation, and direct dispatch allocation
- **With** a fleet and driver logistics management module integrated into order fulfillment.

*(Traducción: Creemos que lograremos reducir en un 20 % los retrasos de transporte y conflictos de asignación si los coordinadores logísticos obtienen control estructurado sobre la disponibilidad de cisternas y conductores con un módulo de gestión de flota y logística de despacho).*

---

**Hypothesis Statement 06 (Historial transaccional y reportes descargables):**
- **We believe we will achieve** a high user engagement with more than 3 report downloads per active company per month and reduced reconciliation discrepancies
- **If** corporate audit supervisors and commercial directors
- **Attain** comprehensive historical records of all completed transactions with exportable audit-ready documentation
- **With** an automated transaction history and downloadable PDF reporting module.

*(Traducción: Creemos que lograremos una alta adopción con más de 3 descargas de reportes al mes por empresa si los auditores corporativos y directores comerciales obtienen un historial completo de transacciones con un módulo de reportes analíticos descargables en PDF).*

#### 1.2.2.4 Lean UX Canvas

<img src="../assets/chapter1/Lean UX/lean-ux-canvas.png" alt="Lean UX Canvas">

## 1.3 Segmentos objetivo

El modelo de negocio de FullTank atiende a dos segmentos empresariales clave del mercado B2B peruano, fundamentados en estudios sectoriales del Instituto Nacional de Estadística e Informática (INEI) y del Organismo Supervisor de la Inversión en Energía y Minería (OSINERGMIN):

### Segmento 1: Empresas compradoras de combustible (Solicitantes)
Empresas medianas y grandes pertenecientes a sectores intensivos en consumo de energía mecánica y térmica, principalmente **construcción civil, minería mediana, transporte de carga pesada, manufactura industrial y agroindustria**.
- **Perfil demográfico y geográfico:** Empresas formalmente constituidas con Registro Único de Contribuyentes (RUC 20), operando en Lima Metropolitana, Callao y provincias con frentes de obra activos. Según el informe de *Demografía Empresarial en el Perú* del INEI (2025), el sector construcción y transporte agrupa a más de 120,000 unidades productivas en el país, de las cuales aproximadamente un 12 % califica como mediana o gran empresa demandante de suministro corporativo continuo.
- **Volumen de consumo:** Consumos periódicos que oscilan entre 15,000 y 500,000 litros de diésel (B5 S-50) o gasolinas industriales al mes, despachados directamente en tanques de obra, plantas de generación eléctrica o cisternas de autoconsumo registradas ante OSINERGMIN.
- **Necesidades clave:**
  - Asegurar el abastecimiento ininterrumpido para evitar la paralización de maquinaria crítica (cuyo costo de inactividad supera los miles de soles por hora).
  - Eliminar errores de transcripción en órdenes y mantener trazabilidad estricta de precios por galón/litro.
  - Centralizar la comunicación con proveedores sin depender de mensajes dispersos de WhatsApp o llamadas.

### Segmento 2: Empresas proveedoras de combustible (Distribuidores autorizados)
Empresas comercializadoras y distribuidoras mayoristas o minoristas de combustibles líquidos y derivados de hidrocarburos, autorizadas formalmente ante el **Registro de Hidrocarburos de OSINERGMIN** bajo la Resolución de Consejo Directivo N.° 150-2024-OS/CD.
- **Perfil demográfico y comercial:** Empresas distribuidoras mayoristas y plantas envasadoras/distribuidoras con flotas de camiones cisterna calibrados y certificados. Según el boletín de *Demanda Nacional de Combustibles Líquidos* de OSINERGMIN (2025), el mercado de distribución B2B en la costa central moviliza más de 180,000 barriles diarios de destilados medios.
- **Capacidad operativa:** Flotas de 3 a 25 unidades de transporte cisterna, con capacidades de carga compartimentada de 1,500 a 10,000 galones por vehículo.
- **Motivaciones y necesidades clave:**
  - Optimizar la recepción y aprobación de órdenes para reducir la saturación operativa del área comercial.
  - Validar comprobantes de pago bancarios antes de comprometer inventario y despachar unidades de transporte.
  - Asignar choferes y unidades vehiculares en función de disponibilidad real y monitorear el cumplimiento de entregas.
  - Ofrecer canales digitales modernos que incrementen la fidelización y retención de clientes corporativos.

### Relación e interdependencia entre los segmentos
La interacción entre compradores y distribuidores configura un ecosistema B2B de alta interdependencia operativa. El comprador no puede arriesgar su continuidad por falta de combustible, y el distribuidor requiere certidumbre transaccional para planificar sus rutas y rotación de cisternas. FullTank se inserta como la plataforma integradora que formaliza la solicitud, valida la disponibilidad de inventario, asegura el respaldo financiero y coordina la entrega en un entorno digital trazable y seguro.

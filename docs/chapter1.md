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

Los Problem Statements parten del recuadro **Business Problem** del Lean UX Canvas y se redactan con la plantilla de Lean UX para iniciativas nuevas (Gothelf & Seiden, 2021): estado actual del dominio, brecha no resuelta, estrategia del producto, enfoque inicial y criterio de éxito. Se formula uno por segmento objetivo.

**Problem Statement 1: empresas solicitantes de combustible**

El estado actual de la distribución de combustibles se ha concentrado en que las empresas medianas y grandes que necesitan combustible de forma constante para su maquinaria, vehículos y equipos gestionen sus pedidos por llamadas telefónicas, correos electrónicos y aplicaciones de mensajería. Estos métodos informales generan desorganización y errores, y no les dan visibilidad en tiempo real del estado de sus pedidos.

Los productos y servicios existentes no resuelven un proceso de pedido ágil, ordenado y confiable en el que el solicitante sepa en todo momento en qué etapa está su combustible.

FullTank abordará esta brecha con una aplicación web de trazabilidad en tiempo real que muestre el estado de cada pedido, envíe alertas sobre los eventos críticos y conserve el historial de pedidos y entregas. El enfoque inicial serán las empresas solicitantes medianas y grandes que dependen del combustible para operar.

Sabremos que tenemos éxito cuando los solicitantes usen FullTank de forma recurrente para seguir sus pedidos y más del 70 % de sus envíos se completen sin necesidad de correcciones posteriores.

**Problem Statement 2: empresas proveedoras de combustible**

El estado actual de la distribución de combustibles se ha concentrado en que las empresas proveedoras que atienden a clientes corporativos e industriales reciban y coordinen los pedidos por llamadas, correos y mensajería. Esto les genera desorganización y errores en las entregas, y les resta visibilidad en tiempo real, lo que afecta su eficiencia operativa y su relación con los clientes.

Los productos y servicios existentes no resuelven una herramienta que les permita optimizar sus operaciones y diferenciarse en un mercado cada vez más competitivo.

FullTank abordará esta brecha con un dashboard de métricas clave, un módulo de gestión de transportistas, alertas automáticas y pagos en línea integrados a cada pedido. El enfoque inicial serán las empresas dedicadas a la distribución de combustible para clientes corporativos o industriales.

Sabremos que tenemos éxito cuando los proveedores gestionen sus pedidos, pagos y transportistas dentro de la plataforma de forma recurrente cada semana y se mantengan activos mes a mes.

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

- Una **aplicación web de trazabilidad en tiempo real** permitirá a solicitantes y proveedores visualizar el estado de cada pedido de combustible.
- Las **alertas y notificaciones en la web** sobre eventos críticos (retrasos, correcciones necesarias y entregas completadas) reducirán los errores y las consultas manuales.
- Un **dashboard interactivo con métricas clave** (envíos completados, tiempos de entrega e incidencias) ayudará a los usuarios a supervisar su operación.
- La **integración con pasarelas de pago en línea** permitirá realizar las transacciones de forma rápida y segura dentro de la plataforma.
- Un **módulo de gestión de transportistas** permitirá al proveedor asignar operadores, hacer seguimiento y evaluar su desempeño.
- El **historial y los reportes descargables** de pedidos y entregas darán a clientes y proveedores un registro verificable de sus operaciones.

#### 1.2.2.3 Lean UX Hypothesis Statements

**Hypothesis Statement 01:**
* *Creemos* que la centralización de los pedidos en nuestra plataforma reducirá el margen de errores causados por problemas de coordinación entre las empresas solicitantes y los proveedores drásticamente.
* *Sabremos* que hemos tenido éxito
* *Cuando* luego de los primeros tres meses de uso se reporte que más de un 70% de los pedidos realizados fueron confirmados sin necesidad de correcciones posteriores.

**Hypothesis Statement 02:**
* *Creemos* que ofrecer más herramientas para el control y seguimiento de pedidos mejorará la satisfacción de los clientes solicitantes.
* *Sabremos* que hemos tenido éxito
* *Cuando* se observe una reducción del 30% en llamadas de seguimiento.

**Hypothesis Statement 03:**
* *Creemos* que la plataforma permitirá a los proveedores optimizar el proceso de gestión de los pedidos y reducir el tiempo que toma cumplir con cada uno.
* *Sabremos* que hemos tenido éxito
* *Cuando* los proveedores logren reducir en un 20% el tiempo promedio entre confirmación y entrega de pedidos.

**Hypothesis Statement 04:**
* *Creemos* que las notificaciones automáticas sobre el estado de los pedidos reducirán la necesidad de una gran cantidad de operadores comerciales de alta disponibilidad.
* *Sabremos* que hemos tenido éxito
* *Cuando* las solicitudes de información por parte de clientes disminuyan en un 40% y el tiempo promedio de atención se reduzca en un 60% tras el primer trimestre de uso.

#### 1.2.2.4 Lean UX Canvas

<img src="../assets/chapter1/Lean UX/lean-ux-canvas.png" alt="Lean UX Canvas">

## 1.3 Segmentos objetivo

### Segmento 1: empresas compradoras de combustible
Empresas medianas y grandes que requieren de combustible de forma constante para el desarrollo de sus operaciones. Utilizan este recurso para alimentar maquinaria, vehículos o equipos, y buscan procesos más ágiles, ordenados y confiables para su gestión de pedidos. Además, mantienen un contrato de exclusividad con un proveedor de combustible, lo que les permite tener un flujo constante de pedidos y una relación comercial estable.

Necesidades:

- Asegurar el abastecimiento oportuno de combustible.
- Reducir errores derivados de la informalidad en los procesos.
- Mantener constante comunicación con proveedores.

### Segmento 2: empresas proveedoras de combustible
Son empresas dedicadas a la distribución de combustibles, atendiendo principalmente a clientes corporativos o industriales. Buscan herramientas que les permitan, optimizar sus operaciones y diferenciarse en un mercado cada vez más competitivo.

Motivaciones:

- Mejorar la experiencia del cliente mediante canales digitales.
- Reducir errores en la entrega por información incompleta o mal gestionada.
- Optimizar la planificación logística y distribución.

### Relación entre los segmentos
La interacción entre las empresas compradoras y proveedoras de combustible configura una relación comercial B2B de alta interdependencia operativa, fortalecida por la existencia de contratos de exclusividad que garantizan un flujo de pedidos constante y una estabilidad a largo plazo. En este marco, las necesidades del comprador por asegurar un abastecimiento oportuno, reducir la informalidad en los procesos y mantener una comunicación constante se alinean de manera directa con las motivaciones logísticas del distribuidor, quien busca optimizar su planificación, minimizar errores en la entrega derivados de la información incompleta y mejorar la experiencia del cliente a través de canales digitales. De este modo, la eliminación de deficiencias en la gestión de pedidos actúa como el nexo integrador que concilia las exigencias de continuidad operativa del comprador con la eficiencia logística y diferenciación competitiva del proveedor.   

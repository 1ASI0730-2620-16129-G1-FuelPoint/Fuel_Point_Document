# Capítulo II: Requirements Elicitation & Analysis

## 2.1. Competidores

En el mercado existen diversas soluciones digitales enfocadas en la gestión de combustible y flotas que compiten de manera directa o indirecta con lo propuesto. Entre ellas destaca **Zavgar**, una plataforma SaaS que ayuda a las empresas con flotas vehiculares a optimizar costos y controlar el consumo de combustible. Otro competidor importante es **FuelCloud**, que ofrece una solución integrada de hardware y software para garantizar seguridad y precisión en el despacho de combustible, principalmente en empresas con tanques propios. Finalmente, **Wialon** se presenta como una plataforma internacional de gestión de flotas que combina monitoreo GPS, análisis operativos y control de combustible, dirigida a compañías logísticas y de transporte.

### 2.1.1. Análisis competitivo.

<table border="2">
  <tr>
    <th colspan="6" style="text-align:left">Competitive Analysis Landscape</th>
  </tr>
  <tr>
    <td colspan="1"><strong>¿Por qué llevar a cabo este análisis?</strong></td>
    <td colspan="5">Este análisis se está llevando a cabo porque queremos conocer las ventajas y desventajas de nuestra aplicación frente a la competencia, y cómo nos diferenciamos de ellas.</td>
  </tr>
  <tr>
    <td colspan="2"><strong></strong></td>
    <td><strong>FullTank</strong><br><img src="./../assets/chapter-2/logo-FullTank.png" height="100"/></td>
    <td><strong>Zavgar</strong><br><img src="./../assets/chapter-2/logo-zavgar.jpg" height="100"/></td>
    <td><strong>FuelCloud</strong><br><img src="./../assets/chapter-2/logo-fuelcloud.jpg" height="100"/></td>
    <td><strong>Wialon</strong><br><img src="./../assets/chapter-2/logo-wialon.jpg" height="100"/></td>
  </tr>

  <tr>
    <th rowspan="3">Perfil</th>
    <td><strong>Visión general</strong></td>
    <td>Plataforma web que digitaliza y estructura el proceso completo de pedido de combustible entre empresas y proveedores.</td>
    <td>SaaS para la gestión de consumo de combustible de flotas, con enfoque en eficiencia, monitoreo y costos.</td>
    <td>Solución con hardware/software para el control físico del despacho de combustible.</td>
    <td>Plataforma de gestión de flotas con control de combustible, GPS y reportes operativos.</td>
  </tr>
  <tr>
    <td><strong>Ventaja competitiva</strong></td>
    <td>Especialización en el flujo completo de pedido, despacho y análisis; integración de pagos y logística; UI intuitiva.</td>
    <td>No requiere hardware; ofrece métricas, control de gastos y reportes sobre consumo.</td>
    <td>Control físico preciso del combustible, monitoreo en tiempo real.</td>
    <td>Seguimiento en tiempo real, visualización de rutas, integración con sensores de combustible.</td>
  </tr>
  <tr>
    <td><strong>¿Qué valor ofrece al cliente?</strong></td>
    <td>Trazabilidad total, eficiencia operativa, reportes de consumo y validación segura de pedidos.</td>
    <td>Optimización de costos y control sobre el uso de combustible en flotas.</td>
    <td>Seguridad y precisión operativa en el control de combustible.</td>
    <td>Trazabilidad de flotas, alertas automáticas, análisis de rutas y consumo de combustible.</td>
  </tr>
  <tr>
    <th rowspan="2">Perfil de Marketing</th>
    <td><strong>Mercado objetivo</strong></td>
    <td>Empresas que solicitan combustible a proveedores.</td>
    <td>Empresas con flotas vehiculares que desean monitorear y reducir el consumo de combustible.</td>
    <td>Empresas con tanques de combustible propios.</td>
    <td>Empresas logísticas, distribuidoras y de transporte de combustible.</td>
  </tr>
  <tr>
    <td><strong>Estrategias de marketing</strong></td>
    <td>Alianzas con proveedores, demostraciones de ahorro, marketing de contenido enfocado en eficiencia.</td>
    <td>Enfoque digital, contenido técnico, integración con proveedores de tarjetas de combustible.</td>
    <td>Ferias industriales, distribuidores, venta consultiva entre empresas.</td>
    <td>Alianzas con distribuidores de GPS, marketing técnico, ferias de transporte.</td>
  </tr>
  <tr>
    <th rowspan="3">Perfil de Producto</th>
    <td><strong>Productos & Servicios</strong></td>
    <td>Plataforma para gestión completa de pedidos, seguimiento, reportes, validación y alertas.</td>
    <td>Plataforma web con módulo de abastecimiento, reportes de consumo, integración GPS y tarjetas.</td>
    <td>Hardware IoT y software para gestión, y control de combustible.</td>
    <td>Plataforma SaaS + app móvil con monitoreo, alertas, mapas y módulos personalizables.</td>
  </tr>
  <tr>
    <td><strong>Precios & Costos</strong></td>
    <td>Modelo SaaS con suscripción escalable según volumen y servicios.</td>
    <td>SaaS con modelos por flota activa o vehículos monitoreados.</td>
    <td>Venta e instalación de hardware + licencias de software.</td>
    <td>Modelo SaaS modular, basado en vehículos activos y funcionalidades activadas.</td>
  </tr>
  <tr>
    <td><strong>Canales de distribución</strong></td>
    <td>Web app responsive, potencial app móvil futura.</td>
    <td>Web app, marketing digital y comunidad de flotas.</td>
    <td>Plataforma web + hardware instalado en sitio.</td>
    <td>Red de partners global, distribuidores locales e integradores de sistemas GPS.</td>
  </tr>
  <tr>
    <th rowspan="4">Análisis SWOT</th>
    <td><strong>Fortalezas</strong></td>
    <td>Enfoque especializado, experiencia de usuario optimizada, integraciones clave, análisis avanzado de consumo.</td>
    <td>Implementación ágil, sin hardware, fácil adopción en empresas medianas.</td>
    <td>Control físico riguroso, solución probada en industrias exigentes.</td>
    <td>Plataforma robusta, cobertura internacional, integración con más de 2,400 dispositivos GPS.</td>
  </tr>
  <tr>
    <td><strong>Debilidades</strong></td>
    <td>Nueva en el mercado, menor reconocimiento de marca, necesita consolidar confianza.</td>
    <td>No gestiona el flujo completo del pedido, enfoque parcial en flotas.</td>
    <td>Alto costo, dependencia de hardware, menor adaptabilidad en mercados emergentes.</td>
    <td>No gestiona pedidos entre proveedor y solicitante, requiere configuración técnica inicial.</td>
  </tr>
  <tr>
    <td><strong>Oportunidades</strong></td>
    <td>Alta informalidad en el sector, digitalización creciente en logística, necesidad de trazabilidad y control.</td>
    <td>Mayor conciencia en eficiencia de flotas y digitalización de costos operativos.</td>
    <td>Nuevos mercados industriales con enfoque en seguridad y control.</td>
    <td>Creciente necesidad de control logístico y monitoreo de distribución en países en desarrollo.</td>
  </tr>
  <tr>
    <td><strong>Amenazas</strong></td>
    <td>Aparición de soluciones similares, resistencia al cambio en empresas tradicionales, competencia ERP.</td>
    <td>SaaS especializados con mayor cobertura funcional (ERP, proveedores, logística).</td>
    <td>SaaS ágiles y sin hardware físico, que ofrecen soluciones más accesibles.</td>
    <td>SaaS más específicos y ligeros, enfocados exclusivamente en la trazabilidad de entregas.</td>
  </tr>
</table>

### 2.1.2. Estrategias y tácticas frente a competidores.

**FuelPoint** aplicará diversas estrategias para afrontar la competencia y aprovechar las oportunidades que ofrece el sector.

#### a. Diferenciación a través de especialización
Una de las principales estrategias de **FuelPoint** es la **especialización en el flujo completo de pedido de combustible**. A diferencia de soluciones como **Zavgar**, que están orientadas principalmente al control y análisis del consumo de combustible en flotas, nuestra plataforma se enfoca en las **interacciones B2B** entre empresas solicitantes y proveedores. Esto nos permite ofrecer un control dedicado del pedido, gestión de la logística, y reportes detallados de consumo y entregas, lo cual no está presente en la mayoría de las plataformas competidoras.

- **Táctica**: Desarrollar funcionalidades para la validación automática de pagos, gestión de stock en tiempo real y la optimización del transporte logrando la automatización de procesos que solo eran logrados de forma manual. Esto crea una ventaja frente a competidores como **FuelCloud**, que se centran más en el control físico del combustible y menos en la administración a nivel operativo.

#### b. Innovación en la interfaz de usuario y experiencia

El sistema de **FuelPoint** está diseñado para ofrecer una **experiencia de usuario optimizada**, algo que **Wialon**, **FuelCloud** y la propia **OSINERGMIN** no abordan en sus plataformas. Al ser una solución especializada y dirigida a una tarea específica, podemos dedicar más recursos en crear una interfaz intuitiva y procesos bien definidos brindando comodidad y seguridad a nuestros usuarios.

- **Táctica**: Diseñar una **interfaz intuitiva y consistente** que permita a los usuarios acceder a reportes de consumo, validar pedidos y coordinar logística con facilidad. Además, ofrecer **soporte y formación continua** para asegurar que los usuarios aprovechen al máximo todas las funcionalidades del sistema.

#### c. Flexibilidad en precios y modelo SaaS escalable
El modelo de precios de **FuelPoint** ofrece **planes escalables basados en suscripción**, lo que hace que sea más accesible para medianas y grandes empresas. Esto es más competitivo frente a **Wialon**, que puede no ser una opción viable para empresas que solo requieren una solución de pedidos de combustible. También es más asequible que **FuelCloud**, que requiere una inversión considerable en hardware, instalación y mantenimiento.

- **Táctica**: Ofrecer un modelo de suscripción flexible y **precios competitivos**, con **múltiples niveles de suscripción** adaptados a las necesidades de diferentes empresas. Esto permitirá que empresas de menor tamaño puedan acceder a la plataforma sin comprometer su presupuesto, a la vez que se asegura el crecimiento a largo plazo a medida que la empresa crece.

#### d. Aprovechamiento de la digitalización en la logística
El sector de la logística está experimentando una transformación digital acelerada. **FuelPoint** se aprovechará de esta tendencia buscando la integración de la plataforma con otras soluciones logísticas (como los sistemas de gestión de vehículos o flotas). De esta forma podemos ofrecer una solución más completa y eficiente.

- **Táctica**: Colaborar con empresas de **gestión de flotas** para optimizar el proceso de asignación de vehículos, cisternas y choferes. También se considerará la posibilidad de integrar **sensores IoT** en los camiones de reparto para un control más preciso sobre el combustible transportado y la entrega.

#### e. Expansión hacia mercados internacionales
Si bien **FuelPoint** está inicialmente orientada a empresas locales, el modelo de negocio y la flexibilidad de la plataforma la hacen ideal para expandirse a **mercados internacionales**. Competidores como **Wialon** ya tienen presencia en mercados globales, pero su enfoque en empresas grandes y sus altos costos de implementación pueden ser una barrera para empresas de menor tamaño, limitando su alcance.

- **Táctica**: Iniciar la expansión en mercados emergentes donde la digitalización en la logística es una necesidad creciente. Esto incluirá la **localización de la plataforma** (idioma, moneda, regulaciones locales) para facilitar la adaptabilidad de los nuevos mercados.

## 2.2. Entrevistas.

### 2.2.1. Diseño de entrevistas.

**A. Proveedores de Combustible**

**Preguntas:**

1. ¿Cuál es su cargo dentro de la empresa proveedora?
2. ¿Qué tipos de clientes atienden principalmente (logística, construcción, minería, agroindustria)?
3. ¿Qué volumen de operaciones realizan mensualmente?
4. ¿Cómo gestionan actualmente los pedidos y contratos de sus clientes?
5. ¿Qué problemas han experimentado con los métodos tradicionales (llamadas, correos, planillas)?
6. ¿Utilizan algún software especializado para ventas o logística?
7. ¿Qué características valoraría más en una plataforma digital para gestionar pedidos?
8. ¿Considera que una solución que centralice cotizaciones, contratos y entregas sería útil para su empresa?
9. ¿Qué tan importante es para ustedes tener reportes históricos y comparativos de ventas?
10. ¿Qué estrategias usan actualmente para fidelizar clientes, y cómo cree que una plataforma como FullTank podría apoyarlos?

---

**B. Empresas Solicitantes**

**Preguntas:**

1. ¿Cuál es su cargo en la empresa?
2. ¿Hace cuánto tiempo trabaja en el sector energético/logístico?
3. ¿Qué volumen de combustible gestionan aproximadamente al mes?
4. ¿Cómo gestionan actualmente la compra y control de combustible?
5. ¿Qué herramientas usan (Excel, llamadas, correos, sistemas propios)?
6. ¿Cuáles son los principales problemas que enfrentan con su sistema actual?
7. ¿Qué tan importante es para usted contar con trazabilidad en tiempo real?
8. ¿Qué dispositivos utilizan para gestionar pedidos (PC, móvil, tablet)?
9. ¿Qué información considera más valiosa al momento de comprar combustible (precio, tiempo de entrega, historial de proveedor, etc.)?
10. ¿Cómo afecta la falta de transparencia en los precios a sus decisiones de compra?
11. ¿Le interesaría recibir notificaciones en tiempo real sobre cambios de precio o estado de sus pedidos?
12. ¿Qué barreras considera que dificultarían implementar una solución digital como FullTank en su empresa?

### 2.2.2 Registro de entrevistas

### 2.2.3 Análisis de entrevistas

### Segmento 1: Empresas Solicitantes de Combustible

### Segmento 2: Proveedores de Combustible

### Análisis Comparativo

### Conclusiones y Definición de Arquetipos

## 2.3 Needfinding

### 2.3.1 User Personas

Los User Personas son perfiles arquetípicos que representan a los usuarios de cada segmento objetivo. Se construyeron a partir de los patrones comunes encontrados en las entrevistas de la sección 2.2: cargos, rutinas, herramientas, frustraciones y metas que se repitieron entre los entrevistados. Se elaboraron en UXPressia y sirven de referencia para el User Task Matrix, los User Journey Maps, los Empathy Maps, el Impact Mapping y el diseño de la aplicación web.

**Segmento 1: empresas solicitantes de combustible**

**Carlos Ramírez Torres** (32 años, Lima) es encargado logístico de una constructora mediana que depende del suministro constante de combustible para operar maquinaria pesada. Tiene más de diez años de experiencia en logística y operaciones. Coordina varios pedidos a la vez, supervisa las entregas y debe evitar que la obra se detenga. Hoy gestiona sus pedidos por llamadas, correo y WhatsApp, por lo que la información queda desordenada y sin trazabilidad.

- **Metas:** reducir en al menos 30 % los retrasos en las entregas, centralizar todos sus pedidos en una sola plataforma, mejorar la comunicación con sus proveedores y decidir con datos.
- **Frustraciones:** falta de una confirmación clara de sus pedidos, errores por mala comunicación, tiempo perdido en seguimiento manual y herramientas desconectadas.
- **Tecnología:** usa laptop y computadora de escritorio con Windows y un celular Android; navega en Google Chrome.
- **Cita:** «Necesito saber exactamente dónde está mi pedido sin tener que estar llamando todo el día».

<img src="../assets/chapter-2/userCarlos.png" alt="User Persona Carlos Ramírez Torres, encargado logístico de una empresa solicitante de combustible" width="600"/>

**Segmento 2: empresas proveedoras de combustible**

**Andrea López Castillo** (28 años, Callao) es gestora de ventas regional en una distribuidora de combustible que atiende a varios clientes industriales. Coordina los pedidos, asigna las rutas de entrega y supervisa que cada despacho se cumpla. Recibe muchas solicitudes al día y las procesa de forma manual, lo que le genera sobrecarga operativa.

- **Metas:** reducir en 50 % los errores logísticos, optimizar las rutas de distribución, disminuir el tiempo de gestión de pedidos y aumentar la satisfacción de sus clientes.
- **Necesidades:** una bandeja única de pedidos, visibilidad del estado de cada despacho y avisos automáticos que eviten responder las mismas consultas.
- **Frustraciones:** exceso de llamadas y mensajes de clientes, dificultad para organizar muchos pedidos, falta de visibilidad en tiempo real y procesos manuales repetitivos.
- **Tecnología:** trabaja principalmente desde laptop y computadora de escritorio con Windows y usa un celular Android en campo; navega en Google Chrome.
- **Cita:** «Si pudiera ver todos los pedidos organizados automáticamente, ahorraría horas de trabajo cada día».

<img src="../assets/chapter-2/userAndrea.png" alt="User Persona Andrea López Castillo, gestora de ventas regional de una empresa proveedora de combustible" width="600"/>

Siguiendo el enfoque de Lean UX (Gothelf & Seiden, 2021), los User Personas priorizan metas, necesidades y comportamientos sobre los datos demográficos, y son documentos vivos: se actualizarán cada vez que las entrevistas o las pruebas de usabilidad aporten nueva evidencia sobre los usuarios.

Ambos perfiles comparten la dependencia de canales desconectados y la necesidad de conocer el estado real de cada pedido. Carlos necesita, sobre todo, registrar y seguir sus pedidos sin llamar. Andrea necesita organizar, validar y despachar muchos pedidos con menos trabajo manual.

### 2.3.2 User Task Matrix

El User Task Matrix recoge las tareas que Carlos y Andrea realizan para cumplir sus objetivos, usen o no FullTank. Para cada tarea se estima su **frecuencia** (con qué periodicidad se realiza) y su **importancia** (cuánto afecta a la continuidad de la operación) en cada segmento. Las valoraciones se basan en lo relatado en las entrevistas y usan la escala Alta, Media y Baja.

| Tarea | Solicitante: frecuencia | Solicitante: importancia | Proveedor: frecuencia | Proveedor: importancia |
|---|---|---|---|---|
| Registrar o recibir pedidos de combustible | Alta | Alta | Alta | Alta |
| Validar la información del pedido | Media | Alta | Alta | Alta |
| Registrar o validar el comprobante de pago | Media | Alta | Alta | Alta |
| Consultar o actualizar el estado del pedido | Alta | Alta | Alta | Alta |
| Modificar o cancelar un pedido | Media | Media | Baja | Media |
| Comparar y elegir proveedores | Baja | Alta | No aplica | No aplica |
| Controlar el nivel de combustible de equipos y tanques | Alta | Alta | No aplica | No aplica |
| Gestionar el inventario de combustible | No aplica | No aplica | Alta | Alta |
| Asignar cisternas y conductores a un despacho | No aplica | No aplica | Alta | Alta |
| Programar y planificar entregas | Baja | Media | Alta | Alta |
| Gestionar varios pedidos a la vez | Media | Media | Alta | Alta |
| Confirmar la recepción del pedido | Media | Alta | Media | Alta |
| Comunicarse entre cliente y proveedor | Alta | Alta | Alta | Alta |
| Recibir o enviar notificaciones | Alta | Alta | Alta | Alta |
| Revisar el historial de pedidos | Media | Media | Media | Media |
| Monitorear consumo o ventas | Baja | Media | Media | Media |
| Generar reportes y métricas | Baja | Media | Media | Media |

**Análisis**

- **Tareas críticas compartidas:** registrar o recibir pedidos, consultar su estado, comunicarse y recibir notificaciones son de frecuencia e importancia altas en ambos segmentos. Por eso forman el núcleo del producto: el flujo de pedidos con estados compartidos y las notificaciones automáticas.
- **Solicitante:** además del pedido, Carlos controla a diario el nivel de sus equipos y tanques, ya que de ello depende cuándo pedir combustible. Esto justifica el módulo de equipos y los accesos directos para crear una solicitud.
- **Proveedor:** Andrea concentra la mayor carga en validar pagos, asignar cisternas y conductores, planificar entregas y gestionar varios pedidos a la vez. Estas tareas justifican la bandeja de solicitudes entrantes, el módulo de flota y el inventario.
- **Tareas de apoyo:** el historial, el monitoreo y los reportes tienen importancia media. Se ofrecerán en módulos secundarios de la aplicación, sin interrumpir el flujo principal.


### 2.3.3 User Journey Mapping

-Segmento 1: Empresas solicitantes de combustible

El User Journey Mapping de Carlos representa el recorrido actual que experimenta como responsable en una empresa constructora, en la gestión del abastecimiento de combustible necesario para la operación de maquinaria pesada. El mapa ilustra el proceso end-to-end, desde la identificación de la necesidad de combustible hasta la evaluación de la entrega y desempeño del proveedor.

En la situación As-Is, Carlos enfrenta un flujo de trabajo manual y poco estructurado: detecta necesidades sin apoyo de alertas, busca proveedores de manera informal, realiza pedidos mediante canales como WhatsApp o correo y da seguimiento a través de llamadas constantes. Esto genera desorden en la información, falta de trazabilidad, retrasos y una alta dependencia de la comunicación manual.

El Journey busca evidenciar los puntos críticos de su experiencia actual, identificando emociones, tareas, fricciones y oportunidades de mejora a lo largo de cada etapa (Awareness, Data Collection, Daily Management, Communication, Reporting y Evaluation). Este análisis servirá como base para diseñar una solución que centralice la información, automatice el registro de pedidos y permita el seguimiento en tiempo real.

 <img src="../assets/chapter-2/journeyCarlos.png" alt="userJourney de Carlos"/>

-Segmento 2: Proveedores de Combustible

El User Journey Mapping de Andrea representa el recorrido actual que experimenta como coordinadora en una empresa distribuidora de combustible, encargada de gestionar múltiples pedidos, coordinar entregas y asegurar el cumplimiento logístico. El mapa ilustra el proceso end-to-end, desde la recepción de pedidos hasta la evaluación del desempeño operativo.

En la situación As-Is, Andrea enfrenta un flujo de trabajo altamente demandante y fragmentado: recibe pedidos por diversos canales, valida información manualmente, organiza rutas sin herramientas automatizadas y mantiene comunicación constante con clientes mediante llamadas y mensajes. Esto genera sobrecarga operativa, errores en la planificación, saturación en la comunicación y limitada visibilidad de métricas clave.

El Journey busca evidenciar los puntos críticos de su experiencia actual, identificando emociones, tareas, fricciones y oportunidades de mejora a lo largo de cada etapa (Awareness, Data Collection, Daily Management, Communication, Reporting y Evaluation). Este análisis servirá como base para diseñar una solución tecnológica que centralice pedidos, automatice la planificación logística y mejore la visibilidad operativa mediante indicadores y dashboards.


 <img src="../assets/chapter-2/journeyAndrea.png" alt="UserJourney de Andrea"/>

### 2.3.4 Empathy Mapping

Para la elaboración de los Empathy Maps, el equipo partió del conocimiento y observaciones recolectadas durante el análisis de los User Persona. Se colocó al centro de cada mapa al usuario correspondiente (Carlos y Andrea) y se respondieron las preguntas claves sobre su entorno, emociones, comportamientos y necesidades.

-Segmento 1: Empresas solicitantes de combustible


 <img src="../assets/chapter-2/empathyCarlos.png" alt="empathyMapping de Carlos"/>


-Segmento 2: Proveedores de Combustible

 <img src="../assets/chapter-2/empathyAndrea.png" alt="empathyMapping de Andrea"/>

## 2.4 Big Picture Event Storming

### Step 1 – Free Exploration (Exploración Libre)

### Step 2 – Structured Organization (Líneas de Tiempo)

## 2.5 Ubiquitous Language

---
title: "Recuperando Nuestro Tiempo: Flujos de Trabajo Prácticos y Seguros de GenAI para Docentes y Personal"
description: "Taller interactivo de desarrollo profesional sobre gobernanza de IA generativa, cumplimiento de FERPA, flujos de trabajo de alivio administrativo y auditoría de programas de estudio con Fuente Única de Verdad (SSoT)."
date: 2026-08-15
type: "workshop"
translationKey: "reclaiming-our-time"
deck_url: "/decks/reclaiming-our-time/"
video_url: "/videos/reclaiming-our-time.mp4"
institutional_alignment_url: "/governance/institutional-alignment/"
contact: "Alan Pruitt"
aliases:
  - /es/talleres/recuperando-nuestro-tiempo/
---

## Recuperando Nuestro Tiempo: Flujos de Trabajo Prácticos y Seguros de GenAI para Docentes y Personal

Este taller interactivo capacita a los docentes y al personal administrativo para aprovechar la inteligencia artificial generativa con seguridad institucional, cumplimiento estricto de FERPA y alineación directa con los estándares de la Fuente Única de Verdad (SSoT).

---

## Video de Presentación del Taller

{{< workshop-video src="/videos/reclaiming-our-time.mp4" vtt="/videos/reclaiming-our-time.vtt" >}}

---

## Presentación Ejecutiva

Utilice las teclas de flecha o los controles en pantalla para navegar por las diapositivas. Presione **L** para activar el puntero láser azul marino institucional.

{{< workshop-carousel >}}

---

## Resumen Visual Ejecutivo y Mapa de Flujo de Trabajo

El modelo del Auditor Soberano establece que ninguna salida de IA generativa se adopta sin verificación rigurosa frente a normas institucionales predefinidas.

### Marco Operativo Central: El Bucle de Misión

El marco del **Bucle de Misión (Patrón / Regla / Resolver)** estructura la interacción:

1. **Patrón:** Identificar la estructura y patrones del caso o tarea administrativa.
2. **Regla:** Aplicar los estándares federales, institucionales o clínicos autorizados.
3. **Resolver:** Generar una solución verificada y libre de retención de datos.

---

## Módulo 1: Fundamento de Políticas y Autenticación Empresarial

- **Mandatos Federales y Título II de la ADA:** Alineación de todos los activos digitales con la normativa del Título II de la ADA del Departamento de Justicia (exigiendo conformidad estricta con WCAG 2.1 Nivel AA en educación superior pública).
- **Postura Institucional:** Adopción de prácticas de IA generativa legalmente sólidas y académicamente rigurosas para lograr un alivio administrativo y pedagógico sustancial.
- **Límite de Autenticación Empresarial:** Evite interfaces de IA de consumo no autenticadas donde las entradas puedan ser recopiladas para entrenar modelos públicos. Inicie sesión siempre con sus credenciales institucionales (SSO):
  - **Google Gemini Enterprise**
  - **Microsoft Copilot Enterprise**
- **Garantía de Privacidad de Datos:** Los acuerdos de licencia empresarial garantizan que los archivos cargados, las actas de reuniones y los borradores de programas de estudio permanezcan aislados del entrenamiento de modelos públicos.

---

## Módulo 2: Demostraciones en Vivo de Alivio Administrativo

Flujos de trabajo prácticos de alto impacto demostrados en vivo para reducir la carga administrativa docente:

1. **Auditoría de Cumplimiento de Sílabos:** Procesamiento de borradores de programas de estudio junto con rúbricas departamentales, políticas institucionales y requisitos de accesibilidad bajo el Título II de la ADA.
2. **Síntesis de Comités y Elementos de Acción:** Transformación de transcripciones directas de reuniones en resúmenes ejecutivos y matrices estructuradas de rendición de cuentas.
3. **Escalamiento de Rúbricas y Retroalimentación Formativa:** Optimización de rúbricas de evaluación y generación de criterios de retroalimentación constructiva manteniendo la supervisión total del profesor.

### Plantilla de Prompt: Matriz de Acciones de Reunión

{{< prompt-card title="Alivio Administrativo / Matriz de Acciones de Reunión" subtitle="Enfoque: Extracción determinista de elementos de acción, responsables y entregables a partir de transcripciones de comités." badge="MATRIZ DE ACCIÓN" badgeClass="ALIVIO ADMIN" >}}
###
[ROL Y CONTEXTO]:
Actúe como Asistente Administrativo Ejecutivo. Transforme las notas no estructuradas del comité o reunión docente en una matriz de ejecución priorizada y procesable.

[REGLAS DE EXTRACCIÓN]:
1. Aísle entregables explícitos, líderes asignados y plazos de entrega.
2. Agrupe los elementos por dominio operativo (Currículo, Cumplimiento, Operaciones, Tecnología).
3. Identifique decisiones no asignadas que requieran seguimiento del liderazgo.
4. No invente detalles; señale explícitamente cualquier ambigüedad.

[NOTAS DE REUNIÓN EN BRUTO]:
###
[INSERTE AQUÍ LAS NOTAS DE REUNIÓN, TRANSCRIPCIONES O PUNTOS DEL COMITÉ]
###

[FORMATO DE SALIDA]:
Proporcione una tabla Markdown con las columnas:
| N.° | Elemento de Acción / Entregable | Responsable | Fecha Límite | Prioridad (Alta/Media/Baja) |
###
{{< /prompt-card >}}

---

## Módulo 3: Micro-Laboratorio Práctico: Arquitectura de Prompts y Límites Estrictos

Aislar las instrucciones de la tarea de las entradas de datos institucionales es esencial para lograr respuestas deterministas y libres de alucinaciones.

- **El Protocolo Delimitador:** Envolver todos los datos institucionales variables en bloques explícitos con tres numerales (`###`) establece un límite infranqueable dentro del prompt.
- **Instrucciones de Retención Cero:** Imponer restricciones negativas explícitas asegura que el modelo funcione estrictamente como un analizador efímero y no como un repositorio de almacenamiento.

### Arquitectura de Prompts: Protocolo de Aislamiento por Delimitadores

{{< prompt-card title="Arquitectura de Prompts Delimitados / Delimiter Protocol" subtitle="Enfoque: Aislamiento de datos con retención cero y límites estrictos usando delimitadores de triple numeral (###)." badge="PLANTILLA DE PROMPT" badgeClass="PROTOCOLO DELIMITADOR" >}}
###
[ROL Y CONTEXTO]:
Actúe como un Auditor Soberano Experto y Especialista en Currículo. Su tarea es evaluar y alinear el contenido institucional con los estándares de la Fuente Única de Verdad (SSoT) sin retener datos del usuario.

[REGLAS OPERATIVAS]:
1. Opere estrictamente dentro de los límites delimitados proporcionados.
2. Coteje el texto de entrada exclusivamente contra los estándares de política proporcionados.
3. Señale brechas de cumplimiento, vectores de accesibilidad faltantes y discrepancias de alineación.
4. Genere los hallazgos en una tabla Markdown estructurada y accionable.

[DATOS DE ENTRADA / TEXTO A AUDITAR]:
###
[INSERTE AQUÍ EL PROGRAMA DE ESTUDIOS, RÚBRICA O TRANSCRIPCIÓN NO ESTRUCTURADA]
###

[DIRECTRIZ DE AUDITORÍA]:
Genere la matriz de auditoría identificando:
- Hallazgo / Brecha
- Referencia de Norma Oficial
- Elemento de Acción para Corrección
###
{{< /prompt-card >}}

---

## Módulo 4: Cumplimiento de FERPA y Enrutamiento Seguro

Protección estricta de los expedientes e información confidencial estudiantil conforme a las leyes federales:

- **Transmisión Cero de PII:** Nunca pegue nombres de estudiantes, números de identificación, calificaciones o datos demográficos sensibles en interfaces de IA.
- **Estándares de Anonimización:** Desidentifique y redacte cualquier trabajo estudiantil o hilo de discusión antes de procesarlo.
- **Imperativo de Supervisión Humana:** Las salidas de la IA sirven como borradores iniciales; las calificaciones definitivas, el diseño curricular y las autorizaciones administrativas siguen siendo responsabilidad humana exclusiva.

---

## Módulo 5: Síntesis, Recursos y Soporte Institucional

### Herramientas Empresariales y Enrutamiento Institucional Oficial

- **Portal Principal de Inteligencia Artificial Responsable:** Acceda a herramientas autorizadas, solicite cuentas empresariales y consulte las directrices oficiales a través del [Portal de Inicio de IA Responsable de la Universidad de Arizona](https://responsibleai.arizona.edu/tools-support/start-here).
- **Soporte y Mesa de Ayuda Institucional de GenAI:** Envíe consultas departamentales, revise evaluaciones de seguridad y privacidad, y acceda a recursos autorizados de IA directamente a través del equipo de IA Responsable.
- **Gobernanza de Datos y Cumplimiento de FERPA:** Consulte las políticas de privacidad y seguridad de la información universitaria mediante el portal de IA Responsable antes de procesar materiales o registros institucionales.

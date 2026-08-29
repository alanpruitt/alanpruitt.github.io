---
title: "Recuperando Nuestro Tiempo: Flujos de Trabajo de GenAI Seguros y Prácticos para Profesores y Personal"
date: 2026-08-29T10:00:00-07:00
publishDate: 2026-08-29T10:00:00-07:00
draft: false
slug: "reclaiming-our-time"
description: "Una guía interactiva de desarrollo profesional de 60 minutos y portal de referencia para flujos de trabajo de GenAI empresariales seguros, arquitectura de delimitadores de prompts y cumplimiento de FERPA/HIPAA."
categories: ["Inteligencia Artificial Generativa", "Gobernanza en Educación Superior", "Talleres", "Desarrollo Docente"]
layout: "workshop-single"
facilitator: "Alan Pruitt"
facilitator_title: "Colega del Campus Designado (DCC - Yuma) y Estratega de IA Generativa"
facilitator_email: "alanpruitt@arizona.edu"
institutional_alignment: "Oficina de IA Responsable, Oficina de Seguridad de la Información (ISO) y la Infraestructura de IA de la Universidad de Arizona"
duration: "60 Minutos"
---

## Video de Presentación del Taller

{{< workshop-video src="/videos/reclaiming-our-time.mp4" vtt="/videos/reclaiming-our-time.vtt" >}}

---

## Presentación Ejecutiva

{{< workshop-carousel >}}

---

## Estructura y Tiempos de la Sesión

<div class="timing-grid">
  <div class="timing-card">
    <span class="timing-span">00:00 - 00:10</span>
    <div class="timing-title">Módulo 1: Ecosistema Empresarial</div>
  </div>
  <div class="timing-card">
    <span class="timing-span">00:10 - 00:30</span>
    <div class="timing-title">Módulo 2: Flujos en Vivo</div>
  </div>
  <div class="timing-card">
    <span class="timing-span">00:30 - 00:45</span>
    <div class="timing-title">Módulo 3: Micro-Lab de Prompts</div>
  </div>
  <div class="timing-card">
    <span class="timing-span">00:45 - 00:55</span>
    <div class="timing-title">Módulo 4: FERPA y Enrutamiento</div>
  </div>
  <div class="timing-card">
    <span class="timing-span">00:55 - 01:00</span>
    <div class="timing-title">Síntesis y Referencias</div>
  </div>
</div>

---

## Módulo 1: Fundamento de Políticas y el Ecosistema Empresarial (10 mins)

* **Postura Institucional:** La Universidad de Arizona apoya la integración de IA legalmente sólida y académicamente rigurosa para proporcionar un alivio administrativo y pedagógico real.
* **Límite de Autenticación Empresarial:** Evite interfaces de IA de consumo no autenticadas donde los prompts pueden ser recopilados para entrenar modelos públicos. Autentíquese siempre mediante su NetID en instancias institucionales:
  * **Google Gemini Enterprise**
  * **U of A GenAI**
  * **Microsoft Copilot Enterprise**
* **Garantía de Privacidad de Datos:** Los acuerdos de licencia empresarial garantizan que las entradas y los documentos subidos no se ingieran en modelos de cimentación públicos, proporcionando un perímetro seguro para el diseño y redacción de cursos.

---

## Módulo 2: Demostración en Vivo de Alivio Administrativo (20 mins)

Tres demostraciones prácticas ejecutadas en vivo durante la sesión del taller:

1. **Auditoría de Cumplimiento de Programas de Estudio:** Ingestión de borradores de programas de estudio junto con las listas de verificación de políticas institucionales para auditar escalas de calificación, declaraciones de accesibilidad bajo el Título II de la ADA y divulgaciones requeridas.
2. **Síntesis de Transcripciones y Puntos de Acción:** Procesamiento de transcripciones de reuniones departamentales o de comités para generar resúmenes ejecutivos, registros cronológicos de decisiones y matrices de rendición de cuentas de forma automática.
3. **Escalamiento de Rúbricas y Retroalimentación Formativa:** Procesamiento de borradores de tareas, rúbricas de evaluación y borradores de estudiantes anonimizados para generar comentarios formativos de alta calidad bajo la supervisión docente.

---

## Módulo 3: Micro-Laboratorio Práctico: Bóveda de Prompts y Delimitadores (15 mins)

### Protocolo de Arquitectura de Prompts

Envuelva todos los datos variables (esquemas de cursos, actas de reuniones, rúbricas) en bloques delimitadores explícitos con tres almohadillas (`###`) para aislar el contexto de las instrucciones, eliminando alucinaciones y desviaciones del modelo.

```plaintext
### ROL Y OBJETIVO ###
Es usted un diseñador de currículo experto y administrador de educación superior.

### CONTEXTO ###
[Inserte aquí el esquema del curso, notas de la reunión o rúbrica de tarea desinfectada]

### TAREA Y RESTRICCIONES ###
Audite el contexto contra los estándares departamentales. Imponga un tono profesional, salida tabular y evite alucinaciones.
```

### Importancia de los Delimitadores

Sin delimitadores explícitos, los LLM a menudo fusionan las instrucciones con el contenido de las variables. Esto conduce a "fugas de instrucción" o "inyección de prompts," donde los datos de entrada que contienen comandos anulan erróneamente el objetivo principal. El uso de delimitadores garantiza límites claros y un procesamiento determinista.

---

## Módulo 4: Cumplimiento de FERPA y Enrutamiento Seguro (10 mins)

* **El Límite de Privacidad del Estudiante (FERPA):** La ley federal protege los expedientes educativos de los estudiantes. Nunca introduzca nombres, correos electrónicos, números de identificación, calificaciones o promedios de estudiantes en interfaces de prompts de IA, ya sean comerciales o empresariales.
* **Flujo de Desinfección de Datos:** Limpie siempre el contenido antes de procesarlo:
  1. Elimine todos los nombres y sustitúyalos por identificadores estándar (por ejemplo, `Estudiante A`, `Estudiante B`).
  2. Retire direcciones de correo electrónico, números telefónicos e identificadores explícitos.
  3. Redacte narrativas descriptivas locales que puedan identificar de forma indirecta a un individuo.
* **La Seguridad Empresarial No Exime de FERPA:** Aunque los sistemas empresariales mantienen la privacidad de los datos en el inquilino de nube de la universidad, exponer registros estudiantiles sin autorización sigue constituyendo un riesgo de acceso indebido bajo las regulaciones federales e institucionales. Limpie las entradas antes de enviarlas.

---

{{< workshop-infographic >}}

---

## Portal de Síntesis y Referencias (5 mins)

### Lista de Verificación Rápida para Docentes

1. **¿Estoy autenticado?** Verifique que su ventana de Gemini o Copilot indique una sesión activa con su cuenta NetID institucional.
2. **¿Está la entrada desinfectada?** Asegúrese de no incluir información personal de estudiantes.
3. **¿Tengo delimitadores activos?** Asegúrese de que todas las variables estén envueltas en bloques `###`.
4. **¿He auditado la respuesta?** Revise con atención los textos generados antes de utilizarlos.
5. **¿Mantengo el control?** Recuerde que la IA funciona como el motor de procesamiento, pero usted es el piloto.

> *"AI Disclosure: This content was synthesized using Google Gemini. Residents must audit all clinical claims against the Source of Truth. AI can make mistakes."*

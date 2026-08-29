---
title: "Declaración de Conformidad de Accesibilidad"
date: 2026-08-28T19:40:00-07:00
description: "Declaración formal de accesibilidad, estado de conformidad WCAG 2.2 Nivel AA y mecanismo de retroalimentación de alanpruitt.com."
layout: "single"
---

## Compromiso con la Accesibilidad Digital

Alan Pruitt está comprometido con garantizar la accesibilidad digital para todos los usuarios, incluidas las personas con discapacidades. Auditamos y optimizamos continuamente esta plataforma para cumplir con los estándares **WCAG 2.2 Nivel AA** y la regla final del **Título II de la Ley sobre Estadounidenses con Discapacidades (ADA - 28 CFR Parte 35)**.

---

### Estado de Conformidad

* **Estándar:** Pautas de Accesibilidad para el Contenido Web (WCAG) 2.2 Nivel AA.
* **Estado Actual:** Totalmente conforme. Todos los flujos principales, ensayos, calculadoras interactivas y recursos visuales cumplen o superan los requisitos de Nivel AA.
* **Pruebas en Integración Continua (CI/CD):** Nuestra plataforma ejecuta un pipeline de validación automatizado con **Axe-core** y **Playwright** en navegadores headless para prevenir regresiones antes de cada despliegue.

---

### Medidas Arquitectónicas de Accesibilidad

* **Jerarquía Semántica HTML:** Las plantillas reservan `<h1>` exclusivamente para el título principal y estructuran el contenido a partir de `<h2>` sin omitir niveles.
* **Tipografía de Alto Contraste:** Los textos cumplen con una relación mínima de contraste de 4.5:1 para texto normal y 3:1 para texto grande en modos claro y oscuro.
* **Controles Interactivos:** Todos los botones, filtros y enlaces cuentan con áreas de contacto mínimas de $44 \times 44\text{px}$ con indicadores visibles `:focus-visible`.
* **Alternativas a Contenido No Textual:** Los diagramas complejos (incluyendo la infografía de Curriculum-as-Code) incluyen transcripciones completas en texto semántico.
* **Anunciadores para Lectores de Pantalla:** Las herramientas interactivas utilizan regiones `aria-live="polite"` para comunicar cálculos dinámicos sin interrumpir la lectura.

---

### Aviso de Independencia Institucional

Los análisis, marcos y ensayos de este sitio corresponden a la práctica profesional independiente de Alan Pruitt y no representan una postura oficial o legal de Arizona Western College o The University of Arizona.

---

### Reporte de Barreras y Retroalimentación

Si encuentra alguna dificultad o barrera de acceso en este sitio, por favor comuníquese indicando la dirección URL y una breve descripción:

**Alan Pruitt**  
Correo electrónico: `alan.pruitt@gmail.com`  
Asunto: `Retroalimentación de Accesibilidad - alanpruitt.com`

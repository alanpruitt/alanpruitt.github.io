---
title: "Plan de Estudios como Código, Cumplimiento de ADA Título II y Refactorización de Accesibilidad a Gran Escala"
date: 2026-08-27T08:00:00-07:00
draft: false
slug: "essay-27"
translationKey: "essay-27"
description: "Cómo implementar canalizaciones de Curriculum-as-Code (CaC) con linters automatizados y paridad SSoT en Canvas LMS para resolver el mandato federal de ADA Título II a nivel institucional."
categories: ["ada-title-ii"]
tags:
  - "ADA Title II"
  - "WCAG 2.2 AA"
  - "Canvas LMS"
  - "CI/CD"
  - "POUR-Audit"
---
## El Mandato Federal: El Fin de las Soluciones Parche

Para las instituciones de educación superior públicas, el reloj del mandato de accesibilidad de **ADA Título II** ya está corriendo. La exigencia federal no deja margen de maniobra: para 2026, cada curso, documento digital, tabla y recurso montado en el LMS debe cumplir a rajatabla con el estándar **WCAG 2.2 AA**.

Durante más de una década, la respuesta tradicional de las universidades ha sido un ciclo interminable y costoso:

* Contratar cuadrillas de consultores temporales para "limpiar" páginas a mano dentro del editor enriquecido del LMS.
* Depender de extensiones comerciales que detectan errores pero no corrigen la causa raíz estructural.
* Dejar que cada semestre el contenido se vuelva a desacomodar en cuanto el profesorado clona o edita una plantilla sin soporte técnico.

Ese modelo artesanal no escala. Tratar de auditar y arreglar miles de páginas curso por curso, haciendo clic botón por botón en la interfaz gráfica de Canvas, es una pérdida monumental de tiempo y presupuesto.

---

## La Tesis: Deuda Técnica y Soberanía con Curriculum-as-Code (CaC)

La única salida viable para los departamentos y los líderes de TI no es parchar la interfaz de usuario, sino tratar el plan de estudios con la misma disciplina con la que se administra el software crítico: **Curriculum-as-Code (CaC)**.

> Cuando el contenido educativo vive como texto estructurado (Markdown semántico), versionado en Git y auditado por *linters* deterministas antes del despliegue, la accesibilidad deja de ser una carga reactiva y se convierte en una garantía de origen (*born-accessible*).

### La Estructura del Pipeline de Refactorización

---

## La Hoja de Ruta: Despliegue de Refactorización en 4 Fases

Para migrar una flota académica completa sin detener la operación del semestre ni sobrecargar al profesorado, la implementación se ejecuta como una operación de ingeniería en cuatro etapas bien definidas:

### 1. Auditoría de Línea Base y Mapeo de Deuda Técnica (Fase 1)

Antes de mover una sola línea de código, se pasa un escaneo automatizado a toda la flota en Canvas para medir el volumen real del problema:

* Extracción masiva del HTML crudo de cada módulo, tarea y página vía la API REST de Canvas.
* Ejecución del script `pour_audit.py` para clasificar fallas críticas: saltos en la jerarquía de encabezados (`<h1>` duplicados o saltos directos a `<h4>`), tablas sin encabezados de alcance (`scope="col"`), y elementos visuales con contraste menor a 4.5:1.
* Generación de un reporte ejecutivo con métricas duras de riesgo legal bajo el mandato de ADA Título II.

### 2. Estandarización de la Fuente Única de Verdad (SSoT) (Fase 2)

Se desconecta la edición manual y se establece el repositorio local como el único origen autorizado del contenido:

* Conversión del material existente a archivos limpios de Markdown (`.md`) estructurados en un repositorio central Git.
* Establecimiento estricto de jerarquía semántica: todo el contenido arranca en `<h2>` para respetar el `<h1>` global reservado por la interfaz de Canvas.
* Eliminación definitiva de estilos en línea (*inline CSS*), fuentes desajustadas y tablas anidadas que rompen la lectura en dispositivos móviles.

### 3. Integración de Tuberías Automatizadas de Control de Calidad (CI/CD) (Fase 3)

La accesibilidad deja de depender de la memoria del diseñador instruccional y pasa a ser resguardada por reglas de compilación automatizadas:

* Integración de `markdownlint-cli2` en el flujo local de desarrollo y en GitHub Actions.
* Configuración de *linters* que rechazan cualquier *commit* que introduzca atributos `alt` vacíos en imágenes informativas, enlaces con textos genéricos ("haz clic aquí") o combinaciones de color que violen WCAG 2.2 AA.
* Pruebas de integración continuas previas a cualquier sincronización institucional.

### 4. Despliegue Determinista y Sincronización por API (Fase 4)

El paso final automatiza la entrega del contenido auditado directamente a las aulas activas:

* Scripts en Python consumen el Markdown validado, lo transforman en HTML semántico de alto contraste y actualizan las páginas de Canvas mediante llamadas seguras a la API REST.
* Eliminación al 100% de la manipulación manual de páginas en el navegador.
* Registro de versiones en Git con historial de cambios (*commits* fechados y firmados), proveyendo evidencia forense inmediata ante cualquier auditoría federal de cumplimiento.

---

## El Resultado Institucional: Accesibilidad por Diseño, No por Remiendo

Resolver el mandato de ADA Título II con parches temporales es una batalla perdida que drena los recursos de la universidad año tras año. Tratar el contenido educativo como infraestructura a través de **Curriculum-as-Code** no solo blinda legalmente a la institución frente a los estándares de 2026, sino que devuelve a los docentes el control absoluto sobre sus materiales.

Al final del día, una arquitectura limpia, rápida y nacida accesible (*born-accessible*) beneficia a todos: el estudiante con lector de pantalla navega sin obstáculos, el estudiante en su teléfono celular carga el contenido al instante sin gastar datos de más, y la institución opera con la certeza de que su infraestructura digital está construida sobre cimientos sólidos.

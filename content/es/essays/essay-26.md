---
title: "Ensayo 26: Navegando el Cumplimiento Aguas Arriba – El Marco de Auditoría POUR en Currículum como Código"
slug: "26-curriculum-as-code-pour-audit-framework"
translationKey: "essay-26"
date: "2026-08-19"
publishDate: "2026-08-19"
draft: false
author: "Alan Pruitt"
categories:
  - "ada-title-ii"
  - "Curriculum-as-Code"
tags:
  - "ADA Title II"
  - "WCAG 2.2 AA"
  - "POUR-Audit"
description: "Cómo operacionalizo los cuatro principios de accesibilidad POUR (Perceptible, Operable, Comprensible y Robusto) mediante verificaciones automatizadas en Git y CI/CD dentro de Currículum como Código."
summary: "Cómo operacionalizo los cuatro principios de accesibilidad POUR (Perceptible, Operable, Comprensible y Robusto) mediante verificaciones automatizadas en Git y CI/CD dentro de Currículum como Código."
substack_url: "https://alanpruitt.substack.com/p/navigating-compliance-upstream-the"
---

## Llevando la Accesibilidad Aguas Arriba Antes de Tocar el LMS

Cuando el Departamento de Justicia de EE. UU. codificó los estándares técnicos de accesibilidad digital bajo **ADA Título II** para las instituciones públicas de educación superior, marcó el fin de los parches reactivos página por página dentro del editor visual del LMS. Corregir manualmente jerarquías rotas de encabezados, atributos `alt` faltantes y bajo contraste de color en cientos de páginas es una trampa administrativa insostenible.

Para lograr un cumplimiento permanente y escalable en mi flota de cursos `EXW`, trasladé la validación de accesibilidad aguas arriba hacia un flujo de ingeniería controlado por versiones: **Currículum como Código (CaC)**. Al mantener los módulos en texto plano Markdown auditado por *linters* automatizados en Git y CI/CD, aplico mi **Marco de Auditoría POUR** antes de que una sola línea llegue a Canvas LMS.

---

## Los Cuatro Pilares POUR Codificados como Reglas Ejecutables

### 1. Perceptible: Verificación Automatizada de Medios y Alto Contraste (`9:1`)

La equidad digital exige que cada diagrama fisiológico, tabla nutricional y bloque de texto sea claramente perceptible:

* **Texto Alternativo Específico (`<= 120` caracteres):** Mis escáneres rechazan etiquetas `<img>` sin atributo `alt`, marcadores vacíos en gráficos informativos o nombres crudos de archivo (`.png`, `.svg`).
* **Guardia de Doble Contraste (`9:1`):** Las validaciones de estilo exigen pares explícitos de color de texto y fondo—como Azul Marino (`#002147`) o Rojo Matador (`#940925`) sobre `#FFFFFF`—superando ampliamente el mínimo de **WCAG 2.2 Nivel AA**.

### 2. Operable: Navegación por Teclado sin Trampas de Foco

Cada simulador clínico e interfaz interactiva debe operar al `100%` mediante teclado y lectores de pantalla móviles, conservando anillos visibles `:focus-visible`, objetivos táctiles mínimos de `44x44px` y eliminando emojis decorativos que generan ruido auditivo.

### 3. Comprensible: Jerarquía Determinista e Higiene Terminológica

* **Anidamiento Secuencial (`<h2>` -> `<h3>` -> `<h4>`):** Todo cuerpo documental inicia estrictamente en `<h2>` (reservando `<h1>` para el título de página en Canvas) sin saltar niveles.
* **Alineación con Fuentes Únicas de Verdad (SSoT):** Los *linters* detectan patrones obsoletos y mantienen la terminología alineada con **PAGA 2018**, **Guías Alimentarias 2025–2030**, **ACSM 12.ª ed.**, **NASM OPT** y lenguaje claro **WCAG 3.0**.

### 4. Robusto: Marcado Semántico Estándar HTML5

El compilador genera tablas accesibles con `<caption>` descriptivo y `<th scope="col">`, listas semánticas y atributos explícitos `lang="es"`, garantizando compatibilidad duradera con tecnologías de asistencia actuales y futuras.

---

> **Aviso de No Endoso Institucional:** La arquitectura Curriculum-as-Code, el Estándar S-A-R y las herramientas de código abierto descritas en este ensayo representan mi ingeniería e investigación docente independiente a través de Webcognita LLC y no constituyen política oficial ni respaldo de Arizona Western College ni de The University of Arizona.

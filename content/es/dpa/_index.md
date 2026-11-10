---
title: "Anexo de Procesamiento de Datos (DPA)"
date: 2026-11-10T08:00:00-07:00
draft: false
layout: "single"
description: "Anexo de Procesamiento de Datos (DPA), cláusula de cumplimiento FERPA, garantía de accesibilidad ADA Título II y gobernanza de IA para contratos institucionales de Webcognita LLC."
---

## Cláusula de Cumplimiento Institucional y Gobernanza de IA

* **Fecha de Entrada en Vigor:** 10 de noviembre de 2026
* **Entidad:** Webcognita LLC (empresa propiedad de veteranos, VOSB) y Alan Pruitt ("Proveedor", "nosotros" o "nuestro")
* **Aplicable A:** Todas las instituciones educativas, colegios comunitarios, universidades, agencias públicas de desarrollo laboral y entidades gubernamentales ("Cliente" o "Institución") que celebren un Contrato Maestro de Servicios, Alcance de Trabajo (SOW), Orden de Compra o licencia de productos digitales con Webcognita LLC.

---

### 1. Propósito, Alcance y Orden de Prelación

Este Anexo de Procesamiento de Datos ("DPA") complementa los [Términos de Servicio de Webcognita LLC](/es/terms/), la [Política de Privacidad](/es/privacy/) y el [Anexo de Propiedad Intelectual y OER](/es/ip-oer/), así como cualquier contrato institucional, Orden de Compra o Alcance de Trabajo (SOW) aplicable. Este DPA garantiza el cumplimiento estricto de los mandatos legales de privacidad de datos, accesibilidad y gobernanza de inteligencia artificial, incluyendo la **Ley de Derechos Educativos y Privacidad Familiar (FERPA, 20 U.S.C. § 1232g; 34 CFR Parte 99)**, el **Título II de la ADA del Departamento de Justicia (28 CFR Parte 35)**, las leyes estatales de privacidad de datos estudiantiles y las políticas institucionales de seguridad informática. En caso de conflicto entre los términos de este DPA y los Términos de Servicio generales, prevalecerán los términos de este DPA.

---

### 2. Cumplimiento de FERPA y Expedientes Educativos

1. **Arquitectura Predeterminada sin Datos Personales (Zero-PII by Design):** Webcognita LLC diseña sus marcos de Currículo como Código (Curriculum-as-Code), infraestructura web estática y simuladores ejecutados en el navegador (`exwtoolkit.com`) para operar sin recopilar, transmitir ni almacenar información de identificación personal (PII) de los estudiantes. Salvo que un Alcance de Trabajo por escrito lo requiera explícitamente, la Institución no necesita proporcionar datos personales estudiantiles a Webcognita LLC.
2. **Designación de Funcionario Escolar (`34 CFR § 99.31(a)(1)(i)(B)`):** En la medida en que Webcognita LLC reciba, acceda o mantenga expedientes educativos (según se definen en FERPA, `34 CFR Parte 99`) en nombre de la Institución bajo un Alcance de Trabajo específico, el Proveedor reconoce que actúa como "Funcionario Escolar" ("School Official") con un interés educativo legítimo y opera bajo el control directo de la Institución con respecto al uso, mantenimiento y manejo de dichos expedientes educativos.
3. **Prohibición de Divulgación No Autorizada (`34 CFR § 99.33`):** Webcognita LLC no utilizará, divulgará ni volverá a divulgar ningún expediente educativo ni información de identificación personal (PII) derivada de registros estudiantiles para ningún propósito distinto al cumplimiento de los entregables contractuales específicos descritos en el Alcance de Trabajo aplicable.
4. **Minimización Estricta de Datos:** El Proveedor recopilará y procesará únicamente el mínimo indispensable de datos institucionales o docentes necesarios para ejecutar servicios de consultoría, capacitación, auditoría de accesibilidad o integración de software.

---

### 3. Gobernanza de Datos de IA, Soberanía Local y Retención Cero

1. **Prohibición Estricta de Entrenamiento de Modelos Fundacionales:** Webcognita LLC certifica explícitamente que **ningún dato del Cliente, entrada de usuario, documento cargado, instrucción (prompt), código fuente ni contenido institucional procesado a través de los sistemas de Webcognita LLC o flujos de trabajo de IA asociados se utilizará jamás para entrenar, ajustar o mejorar modelos públicos o de terceros de aprendizaje automático**.
2. **Inferencia Local Aislada (Air-Gapped) y APIs Empresariales de Retención Cero:** Cualquier modelo de inteligencia artificial o herramienta de auditoría automatizada implementada por Webcognita LLC en relación con contratos institucionales opera exclusivamente mediante: (a) **inferencia en hardware local aislado (`Cero Salida a la Nube`)**, donde todo el cómputo permanece en estaciones de trabajo locales cifradas, o (b) **puntos de enlace API empresariales de retención cero**, donde los datos de entrada y salida se procesan de forma efímera y se eliminan inmediatamente después de resolver la consulta.
3. **Alineación con Estándares Federales de IA y Riesgo:** Todos los flujos de trabajo de gobernanza de IA y entregables instruccionales se alinean con el **Marco de Gestión de Riesgos de IA del NIST (NIST AI RMF 1.0)** y el **Aviso de Capacitación y Empleo (TEN) No. 07-25 del Departamento de Trabajo de los EE. UU. (DOL ETA) (*Marco de Alfabetización en Inteligencia Artificial*)**.
4. **Sin Monetización por Terceros:** Los datos institucionales y activos de propiedad intelectual jamás serán monetizados, agregados para perfilamiento comercial ni compartidos con terceros no autorizados.

---

### 4. Inventario de Subprocesadores y Transparencia en la Cadena de Suministro

Webcognita LLC mantiene un inventario mínimo y transparente de proveedores de infraestructura autorizados utilizados para entregar activos web estáticos, documentación y facturación:

* **Alojamiento Estático y Control de Versiones:** GitHub Pages / GitHub Enterprise (Alojamiento de activos estáticos, repositorios con control de versiones y despliegue automatizado CI/CD).
* **Enrutamiento Perimetral DNS y Seguridad TLS:** Cloudflare, Inc. (Resolución DNS, mitigación DDoS y cifrado de transporte TLS/HTTPS obligatorio).
* **Procesamiento de Pagos (Si Aplica):** Stripe, Inc. (Manejo tokenizado de transacciones financieras conforme a PCI-DSS Nivel 1; las credenciales de tarjetas de pago nunca tocan los servidores de Webcognita LLC).
* **Obligaciones de los Subprocesadores:** Webcognita LLC sujeta a todos los subprocesadores autorizados a estándares de protección de datos y seguridad no menos restrictivos que los descritos en este DPA. Se notificará por escrito a la Institución antes de incorporar cualquier nuevo subprocesador que maneje datos institucionales.

---

### 5. Seguridad de Datos, Cumplimiento de Accesibilidad y Notificación de Incidentes

1. **Salvaguardas Técnicas y Administrativas:** Webcognita LLC implementa salvaguardas administrativas, físicas y técnicas estándar de la industria, incluyendo cifrado obligatorio TLS 1.3 / HTTPS para datos en tránsito, cifrado AES-256 para datos en reposo, autenticación multifactor respaldada por hardware (MFA) para el acceso administrativo y arquitecturas estáticas que eliminan superficies de inyección en bases de datos del lado del servidor.
2. **Estándares de Accesibilidad Digital (`ADA Título II` • `WCAG 2.2 AA` • `Sección 508`):** Todos los activos digitales, materiales curriculares y aplicaciones web entregados por Webcognita LLC están diseñados y auditados continuamente para cumplir con **WCAG 2.2 Nivel AA** (incluyendo umbrales de legibilidad visual de alto contraste `9:1`), el **Título II de la ADA del DOJ (`28 CFR Parte 35`)** y la **Sección 508 de la Ley de Rehabilitación (`36 CFR Parte 1194`)**.
3. **Notificación de Incidentes de Seguridad en 48 Horas:** En caso de una vulneración de seguridad confirmada o razonablemente sospechada que comprometa datos institucionales o expedientes educativos, Webcognita LLC notificará al oficial de adquisiciones y al asesor legal designados por la Institución sin demora injustificada —y en ningún caso más tarde de **cuarenta y ocho (48) horas** tras su descubrimiento—, brindando plena cooperación y telemetría forense para mitigar el incidente.

---

### 6. Devolución de Datos y Eliminación Permanente Certificada

Al vencimiento, rescisión o finalización del Alcance de Trabajo o contrato aplicable:

1. **Eliminación Segura (Plazo de 30 Días):** Webcognita LLC deberá, dentro de los **treinta (30) días naturales** (o antes si la Institución lo solicita por escrito), devolver, eliminar, depurar y destruir de forma segura todos los datos institucionales, registros de comunicaciones confidenciales y archivos educativos de sus sistemas activos y copias de seguridad no archivísticas.
2. **Certificado de Destrucción:** Previa solicitud por escrito de la Institución, un director autorizado de Webcognita LLC proporcionará una certificación formal por escrito confirmando que todos los datos institucionales han sido destruidos de forma permanente y segura.

---

### 7. Ley Aplicable y Jurisdicción Institucional

Este DPA se regirá e interpretará de conformidad con las leyes federales de los Estados Unidos y las leyes estatales de la jurisdicción que rija a la institución educativa o agencia pública contratante (o del Estado de Arizona si no se especifica lo contrario por estatuto), sin dar efecto a los principios sobre conflicto de leyes.

---

### 8. Ejecución Autorizada

Al celebrar un Contrato Maestro de Servicios, Orden de Compra o Alcance de Trabajo con Webcognita LLC, el firmante garantiza que es un representante autorizado de Webcognita LLC y que los compromisos descritos en este Anexo de Procesamiento de Datos son legalmente vinculantes para la organización.

* **Proveedor:** Webcognita LLC (Veteran-Owned Small Business)
* **Director Principal:** Alan Pruitt
* **URL Canónica del DPA:** `https://alanpruitt.com/es/dpa/`
* **Correo Electrónico de Contacto:** `alan.pruitt@gmail.com`

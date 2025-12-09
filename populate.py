import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'comunicacion_project.settings')
django.setup()

from learning.models import Topic, Quiz, Question

# Topics
topics_data = [
    {"title": "Introducción a la Comunicación", "content": "La comunicación es el proceso de transmitir información, ideas, emociones y significados entre individuos, grupos o entidades. Incluye elementos clave: el emisor (quien envía el mensaje), el mensaje (contenido transmitido), el canal (medio utilizado), el receptor (quien recibe), el contexto (situación) y el feedback (respuesta). Puede ser verbal (palabras), no verbal (gestos, expresiones faciales), escrita, visual o digital. Es fundamental en la sociedad para construir relaciones, compartir conocimientos y coordinar acciones.", "order": 1},
    {"title": "Medios de Comunicación", "content": "Los medios de comunicación son canales que facilitan la transmisión de mensajes. Pueden clasificarse en: verbales (hablada, como conversaciones), no verbales (gestos, expresiones faciales, lenguaje corporal), escritos (correos, libros, periódicos), visuales (imágenes, videos, gráficos) y digitales (internet, redes sociales). Cada medio tiene características únicas: alcance, velocidad, interactividad y capacidad para influir en la percepción. Los medios masivos (prensa, radio, TV, internet) llegan a audiencias amplias y juegan un rol crucial en la formación de opinión pública.", "order": 2},
    {"title": "Comunicación Interpersonal", "content": "Es la interacción directa y bidireccional entre dos o más personas, generalmente cara a cara. Requiere habilidades como la escucha activa (prestar atención y responder), la empatía (comprender emociones ajenas), la claridad en la expresión y el manejo de conflictos. Factores como el lenguaje corporal, el tono de voz y el contexto influyen en su efectividad. Es esencial para construir relaciones personales, resolver problemas y fomentar el entendimiento mutuo.", "order": 3},
    {"title": "Comunicación Masiva", "content": "Involucra medios como televisión, radio, periódicos, internet y redes sociales para llegar a grandes audiencias simultáneamente. Características: unidireccional (del emisor al receptor), masiva (amplio alcance), impersonal y a menudo comercial. Influye en la cultura, la política y la economía al formar opiniones, promover productos y difundir información. Desafíos incluyen la desinformación y la concentración de poder en pocas empresas mediáticas.", "order": 4},
    {"title": "Barreras en la Comunicación", "content": "Factores que impiden una comunicación efectiva: físicas (ruido ambiental, distancia), psicológicas (prejuicios, emociones), semánticas (lenguaje ambiguo, jerga), culturales (diferencias en valores), tecnológicas (fallos en equipos) y organizacionales (jerarquías). Superarlas requiere claridad, feedback, adaptación al receptor y uso de canales apropiados. Identificar barreras mejora la efectividad en cualquier contexto comunicativo.", "order": 5},
    {"title": "Industria Cultural y Medios de Comunicación", "content": "Según Theodor Adorno, la industria cultural produce mensajes multiestratificados que manipulan al público a niveles manifiestos (explícitos) y latentes (ocultos). Los mass media no son solo la suma de sus mensajes, sino que incluyen significados superpuestos que colaboran en el resultado. Esta manipulación se organiza para seducir simultáneamente a varios niveles psicológicos, creando una forma de dominación en sociedades desarrolladas.", "order": 6},
    {"title": "Efectos de los Media", "content": "Los medios buscan seducir a los espectadores en varios niveles psicológicos. El mensaje oculto puede ser más importante que el evidente, penetrando en el cerebro sin ser controlado por la conciencia. Cualquier análisis que ignore esta estructura multiestratificada y los efectos de los mensajes latentes se considera limitado y equivocado.", "order": 7},
    {"title": "Manipulación y Dominación", "content": "La industria cultural actúa como forma de dominación en sociedades desarrolladas. Los espectáculos televisivos apuntan a producir mediocridad, inercia intelectual y credulidad, armonizando con credos totalitarios aunque el mensaje superficial sea antitotalitario. Los mensajes aparentan ser frívolos pero ratifican el estado de sujeción, asimilando órdenes sin que el espectador se dé cuenta.", "order": 8},
    {"title": "Estructura Multiestratificada de los Mensajes", "content": "Los mensajes tienen niveles manifiestos (explícitos) y latentes (ocultos). Los latentes escapan a los controles de la conciencia y penetran sin resistencias psicológicas, canalizando la reacción del público. Las relaciones entre estos niveles no son casuales, sino estratégicas para manipular y dominar.", "order": 9},
    {"title": "Exteriorización vs. Interioridad", "content": "El acto de leer una novela se acerca a un monólogo interior, permitiendo una experiencia introspectiva. En contraste, los mass media se orientan hacia la exteriorización con señales ópticas inequívocas que pueden ser aferradas rápidamente con una mirada, priorizando la visualidad sobre la reflexión interna.", "order": 10},
    {"title": "Teoría de la Comunicación de Shannon y Weaver (1949)", "content": "Esta teoría presenta un modelo lineal de comunicación compuesto por seis elementos: fuente (emisor), codificador, mensaje, canal, decodificador y receptor. Incluye el concepto de ruido (interferencias) que puede distorsionar el mensaje. Es un modelo técnico que se enfoca en la transmisión eficiente de información, pero ha sido criticado por ser demasiado simplista al ignorar el contexto social y el feedback bidireccional.", "order": 11},
    {"title": "Modelo de Lasswell (1948)", "content": "Harold Lasswell propuso esta fórmula: ¿Quién dice qué, en qué canal, a quién, con qué efecto? Este modelo analiza la comunicación masiva identificando los componentes clave: el comunicador, el contenido, el medio, el receptor y el impacto. Es útil para estudiar los procesos de comunicación en los medios de masas, aunque no explica el proceso en detalle.", "order": 12},
    {"title": "Teoría de la Agenda Setting (McCombs y Shaw, 1972)", "content": "Los medios no dicen a la gente qué pensar, pero sí qué pensar. Esta teoría explica cómo los medios establecen la agenda de temas importantes, influyendo en la percepción pública de cuáles son los problemas más relevantes. El framing (enmarcado) complementa esta teoría, determinando cómo se presenta la información.", "order": 13},
    {"title": "Teoría de los Usos y Gratificaciones (Katz, Blumler, 1974)", "content": "Esta teoría se centra en el receptor: ¿por qué las personas usan los medios? Propone que los individuos buscan satisfacer necesidades como información, entretenimiento, integración social, identidad personal y escape de la realidad. Es una perspectiva activa del receptor, en contraste con modelos pasivos.", "order": 14},
    {"title": "Teoría de la Espiral del Silencio (Noelle-Neumann, 1974)", "content": "Las personas tienden a no expresar opiniones que perciben como minoritarias por miedo al aislamiento social. Esto crea una 'espiral' donde las opiniones mayoritarias se refuerzan y las minoritarias se silencian. Es relevante en contextos de opinión pública y medios sociales.", "order": 15},
    {"title": "Teoría Hipodérmica o de la Bala Mágica (1920s-1930s)", "content": "Los medios inyectan mensajes directamente en la mente del receptor como una bala, causando efectos inmediatos y uniformes. Aunque desmentida, explica el pánico inicial ante los medios masivos y destaca la influencia potencial de la propaganda.", "order": 16},
    {"title": "Teoría de la Dependencia de los Medios (Ball-Rokeach, DeFleur, 1976)", "content": "La dependencia de los individuos hacia los medios para satisfacer necesidades crea poder social. Cuando hay incertidumbre (como en crisis), la dependencia aumenta, y los medios pueden influir más en actitudes y comportamientos.", "order": 17},
    {"title": "Evolución de los Medios de Comunicación", "content": "La comunicación ha evolucionado desde formas primitivas hasta digitales. Incluye: el servicio postal (siglo XVII), los trenes que facilitaron el transporte de información, el telégrafo (1837) para mensajes eléctricos, la fotografía (1826) para imágenes fijas, el cine (1895) para narrativas visuales, la radio (1920) para audio masivo, el teléfono (1876) para comunicación interpersonal, la televisión (1920s) para video en vivo, e internet (1960s-1990s) para comunicación global digital. Cada medio transformó la sociedad y la forma de compartir información.", "order": 18},
]

for data in topics_data:
    Topic.objects.get_or_create(title=data['title'], defaults=data)

# Quizzes
quizzes_data = [
    {"title": "Evaluación 1: Conceptos Básicos", "questions": [
        {"question": "¿Qué es la comunicación?", "options": ["El proceso de transmitir información", "Un tipo de tecnología", "Un medio de transporte"], "answer": 1},
        {"question": "¿Cuál es un elemento clave de la comunicación?", "options": ["Emisor", "Vehículo", "Edificio"], "answer": 1},
        {"question": "¿Qué incluye el feedback en la comunicación?", "options": ["Respuesta del receptor", "El canal usado", "El mensaje original"], "answer": 1}
    ]},
    # Add more quizzes similarly
]

for quiz_data in quizzes_data:
    quiz, created = Quiz.objects.get_or_create(title=quiz_data['title'])
    for q in quiz_data['questions']:
        Question.objects.get_or_create(quiz=quiz, question_text=q['question'], defaults={
            'option1': q['options'][0],
            'option2': q['options'][1],
            'option3': q['options'][2],
            'correct_answer': q['answer']
        })

print("Data populated")
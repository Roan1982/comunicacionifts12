function showSection(sectionId) {
    const sections = document.querySelectorAll('.section');
    sections.forEach(section => section.classList.remove('active'));
    document.getElementById(sectionId).classList.add('active');
    if (sectionId === 'teoria') {
        initializeTopics();
    }
}

function initializeTopics() {
    const topics = document.querySelectorAll('.topic');
    document.getElementById('total-topics').textContent = topics.length;
    topics.forEach((topic, index) => {
        const checkbox = topic.querySelector('input');
        const saved = localStorage.getItem(`topic-${index}`);
        if (saved === 'true') {
            checkbox.checked = true;
        }
        checkbox.addEventListener('change', () => {
            localStorage.setItem(`topic-${index}`, checkbox.checked);
        });
    });
    updateProgress();
}

function updateProgress() {
    const checked = document.querySelectorAll('.topic input:checked').length;
    document.getElementById('progress-count').textContent = checked;
}

const quizzes = {
    quiz1: {
        title: 'Evaluación 1: Conceptos Básicos',
        questions: [
            {
                question: '¿Qué es la comunicación?',
                options: ['El proceso de transmitir información', 'Un tipo de tecnología', 'Un medio de transporte'],
                answer: 0
            },
            {
                question: '¿Cuál es un elemento clave de la comunicación?',
                options: ['Emisor', 'Vehículo', 'Edificio'],
                answer: 0
            },
            {
                question: '¿Qué incluye el feedback en la comunicación?',
                options: ['Respuesta del receptor', 'El canal usado', 'El mensaje original'],
                answer: 0
            }
        ]
    },
    quiz2: {
        title: 'Evaluación 2: Medios de Comunicación',
        questions: [
            {
                question: '¿Qué es un medio verbal?',
                options: ['Habla', 'Gesto', 'Imagen'],
                answer: 0
            },
            {
                question: '¿Cuál es un ejemplo de comunicación no verbal?',
                options: ['Correo electrónico', 'Expresión facial', 'Libro'],
                answer: 1
            },
            {
                question: '¿Qué medio usa texto escrito?',
                options: ['Televisión', 'Radio', 'Correo'],
                answer: 2
            }
        ]
    },
    quiz3: {
        title: 'Evaluación 3: Barreras en la Comunicación',
        questions: [
            {
                question: '¿Qué es una barrera física en la comunicación?',
                options: ['Ruido ambiental', 'Prejuicios', 'Lenguaje complejo'],
                answer: 0
            },
            {
                question: '¿Cómo se puede superar una barrera emocional?',
                options: ['Ignorarla', 'Usar empatía', 'Cambiar el canal'],
                answer: 1
            }
        ]
    },
    quiz4: {
        title: 'Evaluación 4: Industria Cultural',
        questions: [
            {
                question: 'Según Adorno, ¿qué produce la industria cultural?',
                options: ['Mensajes simples', 'Mensajes multiestratificados', 'Solo entretenimiento'],
                answer: 1
            },
            {
                question: '¿Qué es más importante en los mensajes de los media?',
                options: ['El mensaje evidente', 'El mensaje oculto', 'El canal'],
                answer: 1
            },
            {
                question: '¿Cómo manipulan los media al público?',
                options: ['Solo con mensajes manifiestos', 'A niveles latentes', 'Sin objetivos'],
                answer: 1
            }
        ]
    },
    quiz5: {
        title: 'Evaluación 5: Efectos de los Media',
        questions: [
            {
                question: '¿Qué buscan los medios según Adorno?',
                options: ['Educar', 'Seducir psicológicamente', 'Informar solo'],
                answer: 1
            },
            {
                question: '¿Qué producen los espectáculos televisivos?',
                options: ['Creatividad', 'Mediocridad e inercia', 'Resistencia'],
                answer: 1
            },
            {
                question: '¿Cómo penetran los mensajes latentes?',
                options: ['Con resistencia', 'Sin controles de conciencia', 'Solo conscientemente'],
                answer: 1
            }
        ]
    },
    quiz6: {
        title: 'Evaluación 6: Teorías Clásicas de Comunicación',
        questions: [
            {
                question: '¿Qué incluye el modelo de Shannon y Weaver?',
                options: ['Solo emisor y receptor', 'Emisor, canal, ruido', 'Solo mensaje'],
                answer: 1
            },
            {
                question: '¿Qué pregunta el modelo de Lasswell?',
                options: ['Cómo se siente', 'Quién dice qué, a quién', 'Por qué se comunica'],
                answer: 1
            },
            {
                question: '¿Qué establece la teoría de la agenda setting?',
                options: ['Qué pensar', 'Qué pensar sobre', 'Cómo pensar'],
                answer: 1
            }
        ]
    },
    quiz7: {
        title: 'Evaluación 7: Teorías de Recepción',
        questions: [
            {
                question: '¿Qué satisface la teoría de usos y gratificaciones?',
                options: ['Necesidades del emisor', 'Necesidades del receptor', 'Necesidades del canal'],
                answer: 1
            },
            {
                question: '¿Qué evita la espiral del silencio?',
                options: ['Opiniones mayoritarias', 'Expresar opiniones minoritarias', 'Comunicación directa'],
                answer: 1
            }
        ]
    },
    quiz8: {
        title: 'Evaluación 8: Evolución de los Medios',
        questions: [
            {
                question: '¿Cuál fue el primer medio de comunicación masiva?',
                options: ['Telégrafo', 'Prensa', 'Radio'],
                answer: 1
            },
            {
                question: '¿Qué medio permitió la comunicación interpersonal a distancia?',
                options: ['Fotografía', 'Teléfono', 'Cine'],
                answer: 1
            },
            {
                question: '¿Qué medio revolucionó la comunicación global?',
                options: ['Televisión', 'Internet', 'Radio'],
                answer: 1
            }
        ]
    }
};

function loadQuiz(quizId) {
    const quiz = quizzes[quizId];
    document.getElementById('quiz-title').textContent = quiz.title;
    const questionsDiv = document.getElementById('questions');
    questionsDiv.innerHTML = '';
    quiz.questions.forEach((q, index) => {
        const questionDiv = document.createElement('div');
        questionDiv.className = 'question';
        questionDiv.innerHTML = `
            <p>${q.question}</p>
            ${q.options.map((option, i) => `<label><input type="radio" name="q${index}" value="${i}"> ${option}</label><br>`).join('')}
        `;
        questionsDiv.appendChild(questionDiv);
    });
    document.getElementById('quiz-container').style.display = 'block';
    document.getElementById('results').style.display = 'none';
}

function submitQuiz() {
    const quizId = Object.keys(quizzes).find(id => document.getElementById('quiz-title').textContent === quizzes[id].title);
    const quiz = quizzes[quizId];
    let score = 0;
    quiz.questions.forEach((q, index) => {
        const selected = document.querySelector(`input[name="q${index}"]:checked`);
        if (selected && parseInt(selected.value) === q.answer) {
            score++;
        }
    });
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = `<h4>Resultado: ${score} / ${quiz.questions.length}</h4>`;
    resultsDiv.style.display = 'block';
}
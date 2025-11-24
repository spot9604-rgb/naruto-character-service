from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import random
import uvicorn

app = FastAPI(title="Кто ты из Наруто=")

class Person(BaseModel):
    name: str
    surname: str  
    birth: str
    gender: str

characters = [
    {
        "name": "Наруто Узумаки", 
        "skill": "Расенган", 
        "village": "Коноха",
        "description": "Энергичный и целеустремленный ниндзя, который никогда не сдается!",
        "color": "#FF6B00"
    },
    {
        "name": "Саске Учиха", 
        "skill": "Шаринган", 
        "village": "Коноха",
        "description": "Спокойный и могущественный ниндзя с жаждой мести и силы",
        "color": "#2E5077"
    },
    {
        "name": "Сакура Харуно", 
        "skill": "Сверхчеловеческая сила", 
        "village": "Коноха",
        "description": "Умная и заботливая ниндзя с невероятной силой воли",
        "color": "#E75495"
    },
    {
        "name": "Какаши Хатаке", 
        "skill": "Тысяча лет смерти", 
        "village": "Коноха", 
        "description": "Мудрый и загадочный ниндзя, копирующий техники противника",
        "color": "#6B7280"
    },
    {
        "name": "Хината Хьюга", 
        "skill": "Бьякуган", 
        "village": "Коноха",
        "description": "Скромная и добрая ниндзя с всевидящим глазом",
        "color": "#6A5ACD"
    },
    {
        "name": "Гаара", 
        "skill": "Песочная защита", 
        "village": "Сунна",
        "description": "Сильный и защищающий ниндзя с контролем над песком",
        "color": "#D4AF37"
    }
]

@app.post("/api/naruto")
def naruto_character(person: Person):
    char_index = random.randint(0, len(characters)-1)
    selected = characters[char_index]
    similarity = random.randint(75, 95)
    
    return {
        "character": selected['name'],
        "ability": selected['skill'],
        "village": selected['village'],
        "similarity": similarity,
        "description": selected['description'],
        "color": selected['color']
    }

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    html_content = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Кто ты из Наруто?</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Arial', sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                padding: 20px;
            }
            
            .container {
                max-width: 600px;
                margin: 0 auto;
                background: white;
                border-radius: 20px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                overflow: hidden;
            }
            
            .header {
                background: linear-gradient(135deg, #FF6B00, #FF8C00);
                color: white;
                padding: 30px;
                text-align: center;
            }
            
            .header h1 {
                font-size: 2.5em;
                margin-bottom: 10px;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }
            
            .header p {
                font-size: 1.2em;
                opacity: 0.9;
            }
            
            .form-section {
                padding: 40px;
            }
            
            .form-group {
                margin-bottom: 25px;
            }
            
            label {
                display: block;
                margin-bottom: 8px;
                font-weight: bold;
                color: #333;
            }
            
            input, select {
                width: 100%;
                padding: 15px;
                border: 2px solid #e1e5e9;
                border-radius: 10px;
                font-size: 16px;
                transition: all 0.3s ease;
            }
            
            input:focus, select:focus {
                outline: none;
                border-color: #FF6B00;
                box-shadow: 0 0 0 3px rgba(255, 107, 0, 0.1);
            }
            
            .gender-buttons {
                display: flex;
                gap: 10px;
            }
            
            .gender-btn {
                flex: 1;
                padding: 15px;
                border: 2px solid #e1e5e9;
                border-radius: 10px;
                background: white;
                cursor: pointer;
                text-align: center;
                transition: all 0.3s ease;
            }
            
            .gender-btn.active {
                background: #FF6B00;
                color: white;
                border-color: #FF6B00;
            }
            
            .submit-btn {
                width: 100%;
                padding: 18px;
                background: linear-gradient(135deg, #FF6B00, #FF8C00);
                color: white;
                border: none;
                border-radius: 12px;
                font-size: 18px;
                font-weight: bold;
                cursor: pointer;
                transition: all 0.3s ease;
                margin-top: 10px;
            }
            
            .submit-btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 20px rgba(255, 107, 0, 0.3);
            }
            
            .submit-btn:active {
                transform: translateY(0);
            }
            
            .result-section {
                padding: 40px;
                display: none;
                animation: fadeIn 0.5s ease;
            }
            
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(20px); }
                to { opacity: 1; transform: translateY(0); }
            }
            
            .character-card {
                border-radius: 15px;
                padding: 30px;
                color: white;
                text-align: center;
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            }
            
            .character-name {
                font-size: 2em;
                margin-bottom: 10px;
                font-weight: bold;
            }
            
            .character-ability, .character-village, .character-description {
                margin-bottom: 15px;
                font-size: 1.1em;
            }
            
            .similarity {
                font-size: 1.3em;
                font-weight: bold;
                margin: 20px 0;
            }
            
            .try-again {
                background: rgba(255,255,255,0.2);
                border: 2px solid white;
                color: white;
                padding: 12px 30px;
                border-radius: 25px;
                cursor: pointer;
                margin-top: 20px;
                transition: all 0.3s ease;
            }
            
            .try-again:hover {
                background: white;
                color: #333;
            }
            
            .loading {
                display: none;
                text-align: center;
                padding: 20px;
            }
            
            .spinner {
                border: 4px solid #f3f3f3;
                border-top: 4px solid #FF6B00;
                border-radius: 50%;
                width: 40px;
                height: 40px;
                animation: spin 1s linear infinite;
                margin: 0 auto 20px;
            }
            
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🎭 Кто ты из Наруто?</h1>
                <p>Узнай своего персонажа из вселенной Наруто!</p>
            </div>
            
            <div class="form-section" id="formSection">
                <div class="form-group">
                    <label for="name">Имя:</label>
                    <input type="text" id="name" placeholder="Введите ваше имя">
                </div>
                
                <div class="form-group">
                    <label for="surname">Фамилия:</label>
                    <input type="text" id="surname" placeholder="Введите вашу фамилию">
                </div>
                
                <div class="form-group">
                    <label for="birth">Дата рождения:</label>
                    <input type="date" id="birth">
                </div>
                
                <div class="form-group">
                    <label>Пол:</label>
                    <div class="gender-buttons">
                        <div class="gender-btn" onclick="selectGender('male')">Мужской</div>
                        <div class="gender-btn" onclick="selectGender('female')">Женский</div>
                    </div>
                    <input type="hidden" id="gender" value="">
                </div>
                
                <button class="submit-btn" onclick="calculateCharacter()">Узнать результат!</button>
            </div>
            
            <div class="loading" id="loadingSection">
                <div class="spinner"></div>
                <p>Определяем вашего персонажа...</p>
            </div>
            
            <div class="result-section" id="resultSection">
                <!-- Результат появится здесь -->
            </div>
        </div>

        <script>
            let selectedGender = '';
            
            function selectGender(gender) {
                selectedGender = gender;
                document.querySelectorAll('.gender-btn').forEach(btn => {
                    btn.classList.remove('active');
                });
                event.target.classList.add('active');
                document.getElementById('gender').value = gender;
            }
            
            async function calculateCharacter() {
                const name = document.getElementById('name').value;
                const surname = document.getElementById('surname').value;
                const birth = document.getElementById('birth').value;
                const gender = selectedGender;
                
                if (!name || !surname || !birth || !gender) {
                    alert('Пожалуйста, заполните все поля!');
                    return;
                }
                
                // Показываем загрузку
                document.getElementById('formSection').style.display = 'none';
                document.getElementById('loadingSection').style.display = 'block';
                document.getElementById('resultSection').style.display = 'none';
                
                try {
                    const response = await fetch('/api/naruto', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                            name: name,
                            surname: surname,
                            birth: birth,
                            gender: gender
                        })
                    });
                    
                    const result = await response.json();
                    
                    // Скрываем загрузку, показываем результат
                    document.getElementById('loadingSection').style.display = 'none';
                    showResult(result);
                    
                } catch (error) {
                    console.error('Ошибка:', error);
                    alert('Произошла ошибка. Попробуйте еще раз!');
                    document.getElementById('loadingSection').style.display = 'none';
                    document.getElementById('formSection').style.display = 'block';
                }
            }
            
            function showResult(result) {
                const resultSection = document.getElementById('resultSection');
                
                resultSection.innerHTML = `
                    <div class="character-card" style="background: ${result.color}">
                        <div class="character-name">${result.character}</div>
                        <div class="similarity">Схожесть: ${result.similarity}%</div>
                        <div class="character-ability">⚡ Способность: ${result.ability}</div>
                        <div class="character-village">🏠 Деревня: ${result.village}</div>
                        <div class="character-description">${result.description}</div>
                        <button class="try-again" onclick="tryAgain()">Попробовать снова</button>
                    </div>
                `;
                
                resultSection.style.display = 'block';
            }
            
            function tryAgain() {
                document.getElementById('resultSection').style.display = 'none';
                document.getElementById('formSection').style.display = 'block';
                
                // Сбрасываем форму
                document.getElementById('name').value = '';
                document.getElementById('surname').value = '';
                document.getElementById('birth').value = '';
                document.getElementById('gender').value = '';
                selectedGender = '';
                document.querySelectorAll('.gender-btn').forEach(btn => {
                    btn.classList.remove('active');
                });
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    print("🚀 Запускаю КРАСИВЫЙ сервер Наруто...")
    print("🌐 Открой: http://localhost:8000")
    print("🎨 Теперь с красивым русским интерфейсом!")
    print("✅ Без ошибок со static файлами!")
    uvicorn.run(app, host="0.0.0.0", port=8000)
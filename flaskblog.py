from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'a2da932426973abace82749198178917'

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]
my_posts = [
	{
    "text": "Какие работы из перечисленных относятся к работам на высоте?",
    "answers": [
      {
        "isCorrect": True,
        "text": "Работы, при которых существуют риски, связанные с возможным падением работника с высоты 1,8 м и более"
      },
      {
        "isCorrect": False,
        "text": "Работы, при которых работник осуществляет подъем на высоту 2 м по лестнице, угол наклона которой к горизонтальной поверхности составляет 45°"
      },
      {
        "isCorrect": False,
        "text": "Работы, проводящиеся на площадках на расстоянии  5 м от неогражденных перепадов по высоте более 1,8 м"
      },
      {
        "isCorrect": False,
        "text": "Работы, проводящиеся на площадках на расстоянии 3 м от огражденных перепадов по высоте более 1,8 м при высоте защитного ограждения этих площадок 1,5 м"
      }
    ]
  },
  {
    "text": "С какой инструкцией должен быть ознакомлен работник, приступающий к выполнению работы по наряду-допуску?",
    "answers": [
      {
        "isCorrect": True,
        "text": "С должностной инструкцией или инструкцией по охране труда по профессии"
      },
      {
        "isCorrect": False,
        "text": "С инструкцией по составлению наряда-допуска"
      },
      {
        "isCorrect": False,
        "text": "С инструкцией по монтажу (демонтажу) конструкций с большой парусностью при ветре скоростью более 10 м/с"
      },
      {
        "isCorrect": False,
        "text": "С инструкцией по работе при грозе или тумане, исключающем видимость в пределах фронта работ"
      }
    ]
  }
]


@app.route('/')
def hello_world():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='login', form=form)

if __name__=='__main__':
	app.run(debug=True)
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    webpage = \
        stylesheet + \
        header() + \
        body() + \
        footer() 
    return webpage


def header():
    return f'''
        <header>
            Velkommen til krasjkurs i avansert git
        </header>
        <br/>
    '''

def body():
    return '''
        <div class="body">
            Mål for kurset er at vi skal lære branching, merging, og pull requests

            Hvordan fungerer branching?<br/>
            <a href="https://www.atlassian.com/git/tutorials/using-branches#:~:text=A%20branch%20represents%20an%20independent%20line%20of%20development.&text=The%20git%20branch%20command%20lets,checkout%20and%20git%20merge%20commands">Atlassian</a>
            har en fantastisk guide, les denne. <br/>
        </div>
        <img src="https://wac-cdn.atlassian.com/dam/jcr:389059a7-214c-46a3-bc52-7781b4730301/hero.svg?cdnVersion=1287"/>
        <br/>
        <br/>
    '''

def footer():
    return '''
        <footer>
            Laget av Patrick Monslaup fra Knowit
        </footer>
    '''


stylesheet = '''
    <style>
        body {
            font-size: 20px;
        }

        header {
            font-size: 1.4rem;
            border-bottom: 1px solid black; 
            margin-bottom: 30px;
            padding-bottom: 10px;
        }

        footer {
            margin-top: 30px;
            padding-top: 10px;
            border-top: 1px solid black;
        }
    </style>
'''
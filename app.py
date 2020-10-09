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
        <h2>
            Krasjkurs i code reviews/pull requests
        </h2>
        <p>
            <b>Mål for kurset</b> er at vi skal lære branching, merging, og pull requests<br/>
            Vi har laget en grunnleggende nettside, og ønsker å utvide den med enkel funksjonalitet
        </p>
        <p>
            <strong>Ikke glad i terminal?</strong> <br/>
            Det finnes mange gode grafiske verktøy som gjør git lettere,
            f.eks. GitHub desktop, git kraken, sourcetree, osv.</br>
        <p>
        
        <hr/>
    '''

def body():
    return '''
        <h3>Basics</h3>
        <p>
            Hvis du er ustø på grunnleggende git les en guide på internett etterpå.<br/>
            Git er bransje-standard, og jeg vet mange av dere har brukt det en del allerede så jeg hopper over introduksjonen.<br/>
            <br/>
            <a href="https://www.atlassian.com/git/tutorials/what-is-version-control">Atlassian</a>
            har en fantastisk guide, les denne.<br/>
        </p>

        <hr/>

        <h3>Branching</h3>
        <p>
            <a href="https://www.atlassian.com/git/tutorials/using-branches">Atlassian</a>
            har også en veldig fin guide her, les denne om du vil lære mer. <br/>
        </p>
        <img src="https://wac-cdn.atlassian.com/dam/jcr:389059a7-214c-46a3-bc52-7781b4730301/hero.svg?cdnVersion=1287"/>
        
        <hr/>
        <br/>

        <h3>Merging</h3>
        <p>
            For å merge skriv `git merge <navn på branch>`.<br/>
            En bedre måte å gjøre det på er ved å åpne pull requests
        </p>
        <img src="https://wac-cdn.atlassian.com/dam/jcr:86eba9ec-9391-45ea-800a-948cec1f2ed7/Branch-2.png?cdnVersion=1287"/>
        <img src="https://wac-cdn.atlassian.com/dam/jcr:83323200-3c57-4c29-9b7e-e67e98745427/Branch-1.png?cdnVersion=1287"/>

        
        <hr/>
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
            font-size: 24px;
        }

        footer {
            margin-top: 30px;
            padding-top: 10px;
            border-top: 1px solid black;
        }
    </style>
'''
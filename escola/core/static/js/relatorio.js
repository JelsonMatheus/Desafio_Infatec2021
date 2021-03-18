
(function inicilizar() {
    btnBuscarAlunos = document.getElementById('btnBuscarAlunos');
    btnBuscarTurmas = document.getElementById('btnBuscarTurmas');
    
    btnBuscarAlunos.addEventListener("click", mostrarAlunos);
    btnBuscarTurmas.addEventListener("click", mostrarTurmas);
    
    mostrarAlunos();
    mostrarProfessores();
    mostrarTurmas();
})();


function mostrarAlunos() {
    const tabela = document.getElementById('tabelaAlunos');
    const tabelaBody = tabela.querySelector("tbody")
    
    const turma = document.getElementById('selectTurma').value;
    const url = "consulta-alunos/" + turma + "/";
    
    consultaJSON(url).then( dados => {
        
        tabelaBody.innerHTML = ""
    
        if(dados.alunos.length === 0) {
            tabelaBody.innerHTML = '<tr><td colspan="3">' + 
                'Nenhum aluno encontrado.</td></th>';
        
            return;
        }
    
        for(let i = 0; i < dados.alunos.length; i++) {
            let template = 
                '<tr><th scope="row">' + (i+1) + '</th>'+
                '<td>' + dados.alunos[i].nome + '</td>' +
                '<td>' + dados.alunos[i].serie + '</td></tr>';
            tabelaBody.innerHTML += template;
        }
    })
    .catch(alert);
}


function mostrarProfessores() {

    const tabela = document.getElementById('tabelaProfessores');
    const tabelaBody = tabela.querySelector('tbody');

    const url = "consulta-professores/";
    
    consultaJSON(url).then(dados => {
        tabelaBody.innerHTML = ""
    
        if(dados.professores.length === 0) {
            tabelaBody.innerHTML = '<tr><td colspan="3">' + 
                'Nenhum professor cadastrado.</td></th>';
        
            return;
        }
    
        for(let i = 0; i < dados.professores.length; i++) {
            const professor = dados.professores[i];
            let template = 
                '<tr><th scope="row">' + (i+1) + '</th>'+
                '<td>' + professor.nome + '</td>' +
                '<td>' + professor.turmas.join(', ') + '</td>';
        
            tabelaBody.innerHTML += template;
        }
    })
    .catch(alert);
}


function mostrarTurmas() {
    const tabela = document.getElementById('tabelaTurmas');
    const tabelaBody = tabela.querySelector("tbody")
    
    const serie = document.getElementById('selectSerie').value;
    const url = "consulta-turmas/" + serie + "/";
    
    consultaJSON(url).then( dados => {
        
        tabelaBody.innerHTML = "";
    
        if(dados.turmas.length === 0) {
            tabelaBody.innerHTML = '<tr><td colspan="3">' + 
                'Nenhuma turma encontrada.</td></th>';
            return;
        }
    
        for(let i = 0; i < dados.turmas.length; i++) {
            turma = dados.turmas[i];
            let template = 
                '<tr><th scope="row">' + (i+1) + '</th>'+
                '<td>' + turma.nome + '</td>' +
                '<td>' + turma.series.join("/") + '</td></tr>';
        
            tabelaBody.innerHTML += template;
        }
    })
    .catch(alert);
}


function printDiv(elem) {
    
    const titulo = '<h1 style="text-align: center;"Relatório </h1>';
    const janela = window.open("","janela", "status=1,width=600,height=400");
    
    janela.document.write('<head>' + document.head.innerHTML + '</head>');
    janela.document.write('<body onafterprint="self.close()">');
    janela.document.write(titulo); 
    janela.document.write(elem.outerHTML);
    janela.document.write('</body></html>');
    janela.document.close();
    janela.print();
}


// Realiza Solicitação de dados.
async function consultaJSON(url) {
    const response = await fetch(url);
    const dados = await response.json();
    return dados
}
import re
from tgff_op import tsk_analyze
import CreateFile

def main():
    x = (int(input('Select the graph number:')))
    tgff = open("tgff_files/creds1.tgff", "r")
    tgff_n = tgff.readlines()
    output = open('outputMatrixes/matrixGraph{}'.format(x), 'w')
    inf = []  # Lista que irá armazenar as informações do grafo selecionado.
    tasks, indTasks= [], []  # tasks:lista que irá armazenar o número de tasks encontradas em inf[]|indTasks = lista de tasks independentes.|
    indIndex, depIndex= [],[] #indIndex=Vetor que armazena os índices de tasks independentes. | #depIndex=Vetor que armazena os índices de tasks dependentes
    dep = []  # Lista de dependências de tasks.

    t = re.compile('TASK t\d+_\d+')  # Operador de expressões regulares usado para encontrar as tasks.
    d = re.compile('FROM t\d+_\d+  TO  t\d+_\d+')  # Operador de expressões regulares usado para encontrar dependências.

    for i in range(len(tgff_n)):
        tgff_n[i] = tgff_n[i].splitlines()[0]  # Operação de retirada de \n das linhas do arquivo.

    inf = tsk_analyze.graphSelect(tgff_n, inf, x)
    tasks, dep = tsk_analyze.infExtract(inf, tasks, dep, t, d)
    matDep = tsk_analyze.matrixCreate(len(tasks))
    matDep = tsk_analyze.destList(tasks, dep, matDep)
    indTasks = tsk_analyze.extractInd(tasks, matDep, indTasks)
    indIndex = tsk_analyze.indIndexes(indTasks)
    tsk_analyze.outputMatrix(matDep, tasks, output)

    ##Pareto.paretoCalculate()

    for i in indIndex:
        depIndex = tsk_analyze.depIndexes(i,matDep)
        CreateFile.Envio(i, len(matDep[i]), depIndex)

    print('Indexes of IT:{}'.format(indIndex))
    print('Number of dependent tasks of task{}: {}'.format(indIndex[0], len(matDep[indIndex[0]])))
    print('Dependents of task{}:{}'.format(indIndex[0], depIndex))

    tgff.close()
    output.close()


if __name__ == '__main__':
    main()
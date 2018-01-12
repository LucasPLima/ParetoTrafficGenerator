def matrixCreate(nl):
    matriz = []
    for i in range(nl):
        l = []
        matriz.append(l)
    return matriz

def graphSelect (fileList , graphList,graph_n):
    for i in range(len(fileList)):
        if fileList[i] == '@TASK_GRAPH {}'.format(graph_n) + ' {':
            while (fileList[i] != '}'):
                graphList.append(fileList[i])  # Anexo das informações do grafo selecionado.
                i += 1
            else:
                break
    return graphList

def infExtract (graphList,taskList,depList,taskPattern,depPattern):
    for i in graphList:
        if len(taskPattern.findall(i))==1:
            taskList.append(taskPattern.findall(i)[0].split('TASK ')[1])  #Extrai as tasks existentes em inf.
        if len(depPattern.findall(i))==1:
            depList.append(depPattern.findall(i)[0].split('FROM ')[1].split('  TO  '))  #Extrai as dependências das tasks em inf.
    return taskList,depList

def destList(taskList,depList,matDep):
    for i in range(len(taskList)):
        for j in range(len(depList)):
            if taskList[i] == depList[j][0]: #compara as tarefas ao índice de dependências para criar uma lista de destinatários, com base nas tarefas relacionadas.
                matDep[i].append(depList[j][1]) #indexa ao índice correspondente a tarefa, seus destinatários.
    return matDep

def extractInd(taskList,matDep,indList):
    ocorrencies = 0
    for i in range(len(taskList)):
        ocorrencies = 0 #variável que conta o número de repetições de um elemento i de taskList na matriz de dependências.
        for j in range(len(matDep)):
            for k in range(len(matDep[j])):
                if taskList[i] == matDep[j][k]: #compara os elementos de taskList com cada elemento da matriz.
                    ocorrencies +=1
        if ocorrencies==0:
            indList.append(taskList[i])
    return indList

def outputMatrix(matDep,tasks,arq):
    for i in range(len(matDep)):
        if (len(matDep[i]) > 0):
            for j in range(len(matDep[i])):
                inf = '{}\t'.format(matDep[i][j])
                arq.write(inf)
            for z in range((len(tasks)-1)-len(matDep[i])):
                inf = '0\t\t'
                arq.write(inf)
        else:
            for j in range(len(tasks)-1):
                inf = '0\t\t'
                arq.write(inf)
        arq.write('\n')

def indIndexes(indTasks):
    indexes = []
    for i in range(len(indTasks)):
        indexes.append(int(indTasks[i].split('_')[1]))
    return indexes

def depIndexes(indTask, matDep):
    dep=[]
    for i in range(len(matDep[indTask])):
        dep.append(int(matDep[indTask][i].split('_')[1]))
    return dep
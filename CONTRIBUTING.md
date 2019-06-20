# Guia de Contribuição

## Como contribuir?

Para contribuir com o projeto é muito fácil e cada pouquinho conta! Basta seguir os seguintes passos:

* *Fork* do repositório (apenas para usuários externos)
* Criar [*issues*](CONTRIBUTING.md#política-de-issues)
* Criar [*branchs*](CONTRIBUTING.md#política-de-branches)
* Seguir a política de [*commits*](CONTRIBUTING.md#política-de-commits)
* Submeter [*Pull Request*](CONTRIBUTING.md#política-de-merges-e-pull-requests)


### Política de Issues

As *issues* devem possuir título, descrição, no mínimo um assinante responsável, *labels*,  *milestone*(a *sprint* que deve ser concluída) e *estimated*(puntuação) para as *issues* pontuadas.

As Labels usadas no projeto estão descritas no tópico [Labels](https://github.com/DesenhoSoftware-2018-2/wiki/labels) no Github.

Para criação de issue o [template Issue](issueTemplate.md) deve ser seguido.


### Política de Branches

#### *master*

A branch *master* é a branch de produção, onde ficará a versão estável do projeto. Ela estará bloqueada para commits e para pushs.
Veja a política de merges no tópico [Merges para *master*](CONTRIBUTING.md#merges-para-master).

#### *dev*

A branch *dev* é a branch de desenvolvimento, onde o trabalho das outras branchs será unificado e onde será criada uma versão estável para mesclar com a *master*.
Assim como a *master* ela está bloqueada para commits e pushs.
Veja a política de merges no tópico [Merges para dev](CONTRIBUTING.md#merges-para-dev)</a>.

#### Nome das Branches

As branchs de desenvolvimento de features serão criadas a partir da branch *development* com a nomenclatura padrão `#x_nome_da_issue`, onde o `x` representa o código de rastreio da issue.

### Política de Commits

A issue em questão deve ser citada no commit, para isso, basta adicionar `<numero_da_issue>#`.

```
 Fazendo_guia_de_contribuição_#5
```

** \*\*Por padrão, o caracter `#` define uma linha de comentário no arquivo da mensagem do commit. Para resolver este problema, use o commando:**
```
git config --local core.commentChar '!'
```

Comentário do commit:
```
#5 Fazendo guia de contribuição

Caso desejar adicionar uma descrição mais detalhada do commit, adicione aqui¹
```

Para que ambos envolvidos no commit sejam incluidos como contribuintes no gráfico de commits do GitHub, basta incluir a instrução `Co-authored-by:` na mensagem:

```
#5 Fazendo guia de contribuição

Co-authored-by: Amanda Muniz <amanda.muniiz@outlook.com>
Co-authored-by: Luciana Albuquerque <albuquerqueluciana54@gmail.com>

```


Para commits que encerram a resolução de uma issue, deve-se iniciar a mensagem do commit com `Fix #<numero_da_issue> <mensagem>`, para que a issue seja [encerrada automaticamente](https://help.github.com/articles/closing-issues-using-keywords/) quando mesclada na `master`.

Exemplo de comentário do commit:
```
Fix #5 Finalizando guia de contribuição do projeto
```

Para commits que incluem uma pequena mudança em uma issue que já teve sua resolução encerrada, deve-se iniciar a mensagem do commit com `HOTFIX #<numero_da_issue> <mensagem>`

Exemplo de comentário do commit:
```
HOTFIX #5 Atualizando guia de contribuição do projeto
```

### Política de Merges e Pull Requests

#### Pull Requests

Pull requests devem ser feitos para a branch *dev* seguindo as regras e os passos do tópico [*Merges para dev*](CONTRIBUTING.md#merges-para-dev). No conteúdo do pull request deve haver uma descrição clara do que foi feito.

Deve ser seguido o [template Pull Request](PULL_REQUEST_TEMPLATE.md).

##### Work in Progress

Caso haja a necessidade de atualizar a branch *dev* antes de concluir a issue, o nome do pull request deve conter WIP:<X_nome_da_branch> para que a branch não seja deletada.

#### Merges para *dev*
Os merges para *dev* deverão ser feitos quando a funcionalidade ou refatoração estiverem de acordo com os seguintes aspectos:
- Funcionalidade ou refatoração concluída;
- Funcionalidade revisada por algum outro membro e um administrador.

Para fazer um merge para *dev* os passos a serem seguidos são:
- `git checkout branch_de_trabalho`;
- `git pull --rebase origin master`;
- `git push origin branch_de_trabalho`;
- Abrir pull request via interface GitHub;
- Aguardar Code Review


##### Code Review
O code review deve ser feito por um ou mais membros da equipe que não participaram das modificações.
Após pelo menos uma aprovação de Code Review, Status Check (GitlabCI) o PullRequest poderá ser aceito;

Para aceitar o PullRequest, deve-se usar a opção *merge* no Github.

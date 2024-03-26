from django.db import models
class Pessoa(models.Model): 
  nome = models.CharField(max_length=255, verbose_name="Nome Completo")
  nome_do_pai = models.CharField(max_length=255, verbose_name="Nome do Pai", blank=True)
  nome_da_mae = models.CharField(max_length=255, verbose_name="Nome da Mãe", blank=True)
  cpf = models.CharField(max_length=14, verbose_name="CPF", unique=True)
  data_nasc = models.DateField(verbose_name="Data de Nascimento")
  email = models.EmailField(verbose_name="E-mail")
  cidade = models.ForeignKey('Cidade', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Cidade")
  ocupacao = models.ForeignKey('Ocupacao', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Ocupação")

  class Meta:
    verbose_name = "Pessoa"
    verbose_name_plural = "Pessoas"

  def __str__(self):
    return self.nome

class Ocupacao(models.Model):

  nome = models.CharField(max_length=255, verbose_name="Nome", unique=True)

  class Meta:
    verbose_name = "Ocupação"
    verbose_name_plural = "Ocupações"

  def __str__(self):
    return self.nome


class Cidade(models.Model):

 
  nome = models.CharField(max_length=255, verbose_name="Nome", unique=True)
  uf = models.CharField(max_length=2, verbose_name="UF")

  class Meta:
    verbose_name = "Cidade"
    verbose_name_plural = "Cidades"

  def __str__(self):
    return self.nome


class InstituicaoEnsino(models.Model):


  nome = models.CharField(max_length=255, verbose_name="Nome")
  site = models.URLField(verbose_name="Site", blank=True)
  telefone = models.CharField(max_length=20, verbose_name="Telefone")
  cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")

class Meta:
    verbose_name = "Instituição de Ensino"
    verbose_name_plural = "Instituições de Ensino"

    def __str__(self):
        return self.nome


class AreaSaber(models.Model):
  nome = models.CharField(max_length=255, verbose_name="Nome", unique=True)

  class Meta:
    verbose_name = "Área do Saber"
    verbose_name_plural = "Áreas do Saber"

  def __str__(self):
    return self.nome

class Curso(models.Model):
 
  nome = models.CharField(max_length=255, verbose_name="Nome")
  carga_horaria_total = models.IntegerField(verbose_name="Carga Horária Total")
  duracao_meses = models.IntegerField(verbose_name="Duração (meses)")
  area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Área do Saber")
  instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituição de Ensino")

  class Meta:
    verbose_name = "Curso"
    verbose_name_plural = "Cursos"

  def __str__(self):
    return self.nome


class PeriodoCurso(models.Model):

  nome = models.CharField(max_length=255, verbose_name="Nome", unique=True)

class Meta:
    verbose_name = "Período de Curso"
    verbose_name_plural = "Períodos de Cursos"

    def __str__(self):
        return self.nome

class Disciplinas(models.Model):

    nome = models.CharField(max_length=255, verbose_name="Nome")
area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Área do Saber")

class Meta:
    verbose_name = "Disciplina"
    verbose_name_plural = "Disciplinas"

    def __str__(self):
        return self.nome


class Matricula(models.Model):

  instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituição de Ensino")
  curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
  pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
  data_inicio = models.DateField(verbose_name="Data de Início")
  data_previsao_termino = models.DateField(verbose_name="Data Prevista de Término")

  class Meta:
    verbose_name = "Matrícula"
    verbose_name_plural = "Matrículas"

  def __str__(self):
    return f"Matrícula de {self.pessoa} em {self.curso}"


class Avaliacao(models.Model):


  descricao = models.TextField(verbose_name="Descrição")
  curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
  disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE, verbose_name="Disciplina")

  class Meta:
    verbose_name = "Avaliação"
    verbose_name_plural = "Avaliações"

  def __str__(self):
    return f"Avaliação: {self.descricao} ({self.curso}, {self.disciplina})"


class Frequencia(models.Model):

  curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
  disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE, verbose_name="Disciplina")
  pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
  numero_faltas = models.IntegerField(verbose_name="Número de Faltas")

  class Meta:
    verbose_name = "Frequência"
    verbose_name_plural = "Frequências"

  def __str__(self):
    return f"Frequência de {self.pessoa} em {self.disciplina}"


class Turma(models.Model):
  
  curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
  periodo = models.ForeignKey(PeriodoCurso, on_delete=models.CASCADE)
  ano_letivo = models.IntegerField()
  turno = models.CharField(max_length=255, choices=[("Manhã", "Manhã"), ("Tarde", "Tarde"), ("Noite", "Noite")])
  professor = models.ForeignKey(Pessoa, on_delete=models.SET_NULL, null=True, related_name="turmas_professor")

  class Meta:
    verbose_name = "Turma"
    verbose_name_plural = "Turmas"
    unique_together = ("curso", "periodo", "ano_letivo", "turno")

  def __str__(self):
    return f"Turma: {self.curso} ({self.periodo}/{self.ano_letivo}) - {self.turno}"




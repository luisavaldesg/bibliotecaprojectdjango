from django.db import models

# Create your models here.
class Autor(models.Model): #Hereda de Model
    #Atributos:
    #Primary Key:
    id = models.AutoField(primary_key = True) #AutoIncremental
    #varchars, maximoscaracteres, no pueden estar en blancos, no pueden ser nulos.
    nombre = models.CharField(max_length = 200, blank = False, null = False) 
    apellido = models.CharField(max_length = 220, blank = False, null = False)
    nacionalidad = models.CharField(max_length = 100, blank= False, null= False)
    #Caja texto mas grande.
    descripcion = models.TextField(blank = False, null = False) 
    estado = models.BooleanField('Estado', default= True) #true= listado
    fecha_creacion = models.DateField('Fecha de creación', auto_now= True, auto_now_add= False)
    #Otros tipos campos: IntegerField. JSONField, URLField, ImageField, FileField, BooleanField

    #Cambiar como saldrá en el sitio de admin django (buenas practicas)
    class Meta: #metadatos, clase extra para datos de nuestro modelo.
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre'] #Ordene por nombre alfabeticamente

    #Identificar cada objeto creado del modelo.
    def __str__(self):
        return self.nombre #Por cada objeto muestre su nombre

# === RELACIONES === #
#OneToOne. --> OneToOneField. Ejemplo --> Un libro tenga un solo libro y viceversa.
#OneToMany(*) --> Foreign Key. Ejemplo --> Un libro puede tener varios libros, pero un libro solo pertenece a un libro.
#ManyToMany --> ManyToManyFIeld. Ejemplo --> Un libro puede tener varios libros, un libro puede ser escrito por varios autores.

class Libro(models.Model):
    id = models.AutoField(primary_key= True)
    titulo = models.CharField('Titulo', max_length=255, blank=False, null= False)
    fecha_publicacion = models.DateField('Fecha de publicación', blank=False, null=False)
    #Relacion
    #autor_id = models.ForeignKey(Autor, on_delete= models.CASCADE)
    #autor_id = models.OneToOneField(Autor, on_delete= models.CASCADE) #on_delete: elimine registro en ambos lados, por cascada
    autor_id = models.ManyToManyField(Autor)

    #auto_now --> Campo se añade solo cada creacion o modificacion.
    fecha_creacion = models.DateField('Fecha de creación', auto_now= True, auto_now_add= False)

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ['titulo']

    def __str__(self):
        return self.titulo #muestre por titulo
    
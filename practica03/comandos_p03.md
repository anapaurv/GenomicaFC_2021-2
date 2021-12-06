# Comandos de la Práctica 03
**Ana Paula Rubio Vargas**

## Parte I
**Respuesta 1:** Creación de directorios y archivos.
Comandos: 
%cd Desktop
%mkdir GenomicaComputacional
%cd GenomicaComputacional
%mkdir aprubio_p03
%touch comandos_p03.md

**Respuesta 2:** Tipo de shell.
Comando: %echo $0
-zsh

**Respuesta 3:** Creación de directorios para proyecto bioinformático.
Comandos: %mkdir -p data/filtered data/raw_data meta scripts figures archive

**Respuesta 4:** Nombre y organización de los archivos.
Como nos dice el repositorio que consultamos, todos los proyectos bioinformáticos deben estar organizados de manera que las personas que consulten este proyecto tengan lo necesario para poder reproducirlo de una manera completa y correcta.
Los nombres de los directorios los elegimos así ya que:
**Data:** Contiene los datos y este puede subdividirse a su vez en subdirectorios de modo que los datos en crudo estén en un solo directorio y los que se vayan modificando por análisis subsecuentes estén en otros. Aquí incluimos nuestros subdirectorios *filtered* y *raw data*
**Meta:** Aquí se guardan todos los metadatos, y si bien puede ir dentro del directorio de data, aquí se pueden guardar los documentos necesarios para procesar los datos.
**Scripts:** Aquí se guardan todos los scripts necesarios para correr el proyecto. Esta carpeta es obligatoria.
**Figures:** Aquí va el código que se usa para la creación de las figuras de nuestro proyecto.
**Archive:** Este no se debe subir al repositorio, pero es util para guardar archivos que aunque bien no son de total utilidad para el proyecto, no deben desecharse por completo.

## Parte II
**Respuesta 1:** Creación de archivos .sh
%cd Scripts
%cat delay.sh
#!/bin/bash
echo "Después de la Parte I. necesito un descanso de exactamente 30 segundos."

**Respuesta 2:** 
%chmod u=xrw,g=r,o=r delay.sh

**Respuesta 3:** Verificar permisos y ejecutar el archivo
%ls -l@ delay.sh
%sh delay.sh
Después de la parte I. necesito un descanso de exactamente 30 segundos.

**Respuesta 4:** Dar pausa de 30 segundos. Nuestro archivo queda entonces de la forma
#!/bin/bash
echo "Después de la Parte I. necesito un descanso de exactamente 30 segundos."
sleep 30
echo "Ya puedo continuar!"

**Respuesta 5:** Matar un proceso.
Cambiamos sleep 30 por sleep 300 y usamos los siguientes comandos
%sh delay.sh & ps
 PID TTY           TIME CMD
 60454 ttys000    0:00.05 -zsh
60484 ttys000    0:00.00 sh delay.sh
%kill 60454

## Parte III
**Respuesta 1:** Resumen del video sobre la estructura del sars-cov-2
%cd meta
%touch SarsCov-2.txt

**Respuesta 2:** Renombrar y mover archivos.
Renombramos los archivos 
%mv sequence.fasta sarscov2_genome.fasta
%mv sequence.gff3 sarscov2_genome.gff3
%mv sequence-2.fasta splike_c.faa
%mv sequence-3.fasta splike_b.faa
%mv sequence-4.fasta splike_a.faa

## Parte IV
**Respuesta 1:** Ligas simbólicas.
%ln -s /Users/anapau/Desktop/GenomicaComputacional/aprubio_p03/data/raw_data/splike_a.faa /Users/anapau/Desktop/GenomicaComputacional/aprubio_p03/data/filtered
%ln -s /Users/anapau/Desktop/GenomicaComputacional/aprubio_p03/data/raw_data/splike_b.faa /Users/anapau/Desktop/GenomicaComputacional/aprubio_p03/data/filtered
%ln -s /Users/anapau/Desktop/GenomicaComputacional/aprubio_p03/data/raw_data/splike_c.faa /Users/anapau/Desktop/GenomicaComputacional/aprubio_p03/data/filtered

**Respuesta 2:** Creación del archivo glycoproteins.faa
%cd data/filtered
%touch glycoproteins.faa

**Respuesta 3:** Obtenemos la primera linea de cada uno de los archivos.
%head -1 splike_*.faa
==> splike_a.faa <==
>pdb|6VXX|C Chain C, Spike glycoprotein

==> splike_b.faa <==
>pdb|6VXX|C Chain C, Spike glycoprotein

==> splike_c.faa <==
>pdb|6VXX|C Chain C, Spike glycoprotein

**Respuesta 4:** Redireccionando el comtenido de los archivos.
%cat splike_a.faa splike_b.faa splike_c.faa > glycoproteins.faa

**Respuesta 5:** Movemos los archivos splike_*.faa a archive
%mv splike_*.faa /Users/anapau/Desktop/GenomicaComputacional/aprubio_p03/archive
Y observamos que sucede con las ligas simbólicas

**Respuesta 6:** Explorando los archivos sarscov2_genome.fasta y sarscov2_assembly.fasta.gz
En este último se descomprime con el nombre contigs.fasta, por lo que así lo llamé en mi terminal
%head -3 sarscov2_genome.fasta
>NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome
ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAA
CGAACTTTAAAATCTGTGTGGCTGTCACTCGGCTGCATGCTTAGTGCACTCACGCAGTATAATTAATAAC

%head -3 contigs.fasta
>NODE_1_length_264_cov_161.042781
CACAAATCTTAACACTCTTCCCTACACGACGCTCTTCCGATCTACGCCGGGCCATTCGTA
CGAACCGATACCTGTGGTAAAGGGTCCTACTGTATGGTGGTACACGAGTAGTAGCAAATG

**Respuesta 7:** Buscando el caracter '/>/' en ambos archivos
%awk '/>/' sarscov2_genome.fasta
>NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome
Este archivo solo tiene un header.
Mientras que en el archivo contigs.fasta, al correr el comando
%awk '/>/' contigs.fasta
Nos regresa 35 lineas, de forma que este archivo tiene 35 headers.

**Respuesta 8:** Patrón de secuencias
%head -12 SRR10971381_R2.fastq
@SRR10971381.512_2
CGTGGAGTATGGCTACATACTACTTATTTGATGAGTCTGGTGAGTTTAAAGTGGCTTCACATATGTATTGTTCTTTCTACCCTCCAGATGAGGATGAAGAAGAAGGTGATTGTGAAGAAGAAGAGTTTGAGCCATCAACTCAATATGAGT
+
/FFFA/A/FFFF66FFFFFF/FF/FFFFFFFFFFFFF/AFFF6FFFA6FFFFF/FFFFFFFFFFFFFFFFFF/FF/FFFFFA/FFF/FFF/A/AFA/FFFFF/=F/F/F/AFAFF//A/AFF//FFAF/FFF=FFAFFFA/A/6=///==
@SRR10971381.556_2
TTTGTAAAAATAAAATAAAAAAAATAAAAATAATATATTAAAAAAAGATAAATAAAAAAATGAACAATTAATAAAAAAAAAAAAAAAAAAAAATTAAAAAAAAAAAAAAAAAAAATAAAAAAAAAAAAAAATAAAAAAAAAATTATAAAA
+
6AFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF/FFFAFFFFFF/FFA/FF=F//=FF/FFFFFFFFFFFFFA/FFFF/FF/FA//F/FFFFFFA/=FFFFF/FFFF/F=FFFAFF///FFFFA/FF/6//////=/
@SRR10971381.1428_2
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
+
FFFFFFFFFFFFAFFFAFFFFFF6A//F//FFF
El patrón que podemos observar nos ayuda a diferenciar entre los tipos de secuencia es que inician con '@', por lo que haciendo la busqueda obtenemos 
%awk '/@/' SRR10971381_R2.fastq
Al correr este nos regresa 130,022 registros, por lo que en el archivo encontramos 130,22 secuencias.

**Respuesta 9:** Diferencias entre formatos.
El formato FASTA que puede tener tanto terminación .faa como .fasta, nos sirve tanto para secuencias de ADN como de ARN, mientras que los archivos con extensión .fastq son archivos que de igual forma tienen formato FASTA más el puntaje de “Q"uality de cada base ("FastQ”).
En este caso podemos observar que nuestros archivos son de nucleotidos debido a su estructura.

**Respuesta 10:** Diferencias al usar less y less -S
Cuando abrimos el archivo usando less nos da los datos en forma de lista mientras que cuando abrimos el archivo con less -S nos los abre en forma de tabla.

**Respuesta 11:** Filtrando el archivo
usando awk con el comando
%awk '($3 == "gene"){count++} END{ print count }' sarscov2_genome.gff3
11
Nos regresa que hay 11 genes en nuestras listas.
La diferencia entre gene y cds es que gene representa una región completa de DNA responsable de todos los productos del RNA, mientras que CDS comprende sólo la región que codifica la proteína.

## Parte V
**Respuesta 1:** Creación de liga simbólica
%ln -s /Users/anapau/Desktop/GenomicaComputacional/aprubio_p03/data/raw_data/sarscov2_genome.gff3 /Users/anapau/Desktop/GenomicaComputacional/aprubio_p03/figures

**Respuesta 2:** Identificar categorías
%awk '/^[^$#]/{count[$3]++} END {for (word in count) print word, count[word]}' sarscov2_genome.gff3 >> barplot_data.txt






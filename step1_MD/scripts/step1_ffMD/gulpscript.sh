#!/bin/bash
#$ -N gulp_0400_GlOpt
#$ -q iqtc04.q
#$ -pe smp 12
#$ -S /bin/bash
#$ -cwd
#$ -o test.out
#$ -e test.err
##$ -m e
##$ -M daniel.reydereyes@gmail.com

# Load the modules needed
. /etc/profile
module load gulp/5.2_gcc_ompi

export PATH=$PATH:/home/g16recio/PhD/ff_gulp
module load /home/g16recio/PhD/ff_gulp

# Copy inputs and files needed to the directory where the jobs will run
export DIR=$PWD
cd $TMPDIR/
cp $DIR/* .

# Run the job
export OMP_NUM_THREADS=1
ulimit -l unlimited

mpirun -np 12 gulp < TiO2_04_H2O_0.gin > TiO2_04_H2O_0.gout

# Copy the results to our home directory

cp -r *  $DIR/


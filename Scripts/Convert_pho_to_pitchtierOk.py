#carico le librerire
# import nltk, re, re, os
# import re
# import codecs
# import sys
import csv
# prefixDir: path to the experiment's folder
prefixDir = "/Users/lettres/Dropbox/expoWhInSituPerception/expWhInSPerception/EXP_perception_contours_finaux-master/ForMBROLA/"

# dirPho: directory with the .pho files to be processed
dirPho = "Files_SAMPA_original_interpolatedProva/"
dirPho = prefixDir + dirPho

# dirOutput: output directory where the .PitchTier will be written
dirOutput = "canc/"
dirOutput = prefixDir + dirOutput


### list the files with the relevant exension in the folder at issue
def lista_file_dir (percorso='/Users/lettres/Dropbox/giovanni senza terra/scripots/corpusparis/trs', estensione='mare'):
    conta = 0
    lfile = []
    import os
    for file in os.listdir(percorso):
        if file.endswith(estensione):
            #print(file)
            conta = conta+1
            lfile.append(file)
    
    #print ('n. ',conta,' di tipo .',estensione)
    return lfile
  
# listPho: list of the .pho files to be processed   
listPho =lista_file_dir(dirPho,'pho')



listFileNoExt = [w.replace('.pho', '') for w in listPho]

totfile = (len (listFileNoExt))
print (totfile)
# cycle for each file
for nf in range(0, totfile):

    ###### open the Pitchtier in output
    pitchTierPath = dirOutput+listFileNoExt[nf]+".PitchTier"
    pitchTierOutput = open(pitchTierPath, "w+")
    print (listFileNoExt[nf])
    ###### open filepho in input
    filepho = dirPho+listFileNoExt[nf]+".pho"
    print (filepho)

   ## write down the head lines of the PitchTier  
    l1= "File type = \"ooTextFile\""
    pitchTierOutput.write(l1)
    pitchTierOutput.write('\n')
    l2= "Object class = \"PitchTier\""
    pitchTierOutput.write(l2)
    pitchTierOutput.write('\n')
    pitchTierOutput.write('\n')
    pitchTierOutput.write("xmin = 0 ")
    pitchTierOutput.write('\n')


    ## querying the .Pho file
    with open(filepho) as f:
        reader = csv.reader(f, delimiter="\t")
        matrixpho = list(reader)
        nrows = len (matrixpho)
        totdur = 0
        #print (nrows)
        for r in range(0, nrows):
            ncol = len(matrixpho[r])
            #print (ncol)
            dur = matrixpho[r][1]
            dur = int(dur)
            totdur = totdur + dur
        totdur = (totdur/1000)
        #print (totdur)                  ########### totalduration value to write
        xmax = "xmax = "+ str(totdur)+ " "
        pitchTierOutput.write(xmax)
        pitchTierOutput.write('\n')
            
        ###################################
        # counting the f0 observations available, i.e. (points : size) in praat
        totpoints = 0
        for r in range(0, nrows):
            ncol = len(matrixpho[r])
            ncol = ncol - 2
            ncol = ncol /2
            totpoints = totpoints + ncol
            totpoints = int(totpoints)
        #print ("totpoints=",totpoints)
        l6 = ("points: size = ")
        l6 = l6 + str(totpoints) + " "
        pitchTierOutput.write(l6)
        pitchTierOutput.write('\n')
        ###################################
        # creating a vector with the absolute starttime (or better... the endtime)
        #of each segment
        # inizializing the list "startlist"
        startlist = []
        dur = 0.0
        starttime = 0.0
        for r in range(0, nrows):
            dur = matrixpho[r][1]
            dur = float(dur)
            #print (dur)
            starttime = starttime + dur
            #print (starttime)
            startlist.append(starttime)
        #print (startlist)
        #print (len(startlist))
        #print (nrows)
        ###################################
        # creating the matrix with the pitch observations: 
        # a fake tuple formed by n. observation, instant (from 0), f0
        pitchmatrix = []
        nobs = 0
        #print (nrows)
        for r in range(0, nrows):
            ncol = len(matrixpho[r])
            if ncol > 2:
                for c in range (2, ncol):
                    cell = float(matrixpho[r][c])
                    # if the n.col is even, then it's a % of duration
                    # if the n.col is odd ("even n.col" + 1),
                    # then it reports the f0 value for the istant defined in n.col
                    if c % 2 == 0:
                        #print ('cell', cell)
                        dursegment = float(matrixpho[r][1])
                        #print ('dur',dursegment)
                        durSlice = ((dursegment/100) * cell)
                        # since startlist actually reports in each line
                        # the endtime of each segement (rather the actual startime)
                        # the starttime must be recalculated: endtime - durtime 
                        instant = ((startlist[r]-dursegment) + durSlice)
                        #print (instant)
                        nobs = (nobs + 1)
                        #print (totpoints, nobs)
                        colhz = c + 1
                        hz  = float(matrixpho[r][colhz])
                        #print (nobs, instant, hz)
                        lnumobs = ("points ["+str(nobs)+"]:")
                        pitchTierOutput.write(lnumobs)
                        pitchTierOutput.write('\n')
                        instant = instant /1000
                        lvalIst = ("    number = "+str(instant)+" ")
                        pitchTierOutput.write(lvalIst)
                        pitchTierOutput.write('\n')
                        #print (lvalIst)
                        lvalF0 = ("    value = "+str(hz)+" ")
                        pitchTierOutput.write(lvalF0)
                        pitchTierOutput.write('\n')
                        #print (lvalF0)

        pitchTierOutput.close()


                        
        
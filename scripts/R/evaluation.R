library('NormalyzerDE')

jobName <- 'plasma1'
outDir <- '../../data/original_data'
dataFp <- '../../data/original_data/plasma1.tsv'
designFp <- '../../data/original_data/plasma1_design.tsv'

normalyzer(jobName=jobName, designPath=designFp, dataPath=dataFp, outputDir=outDir, sampleCol='sample', groupCol = 'group')


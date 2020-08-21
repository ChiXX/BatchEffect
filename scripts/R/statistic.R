library('NormalyzerDE')

outDir <- "../../data/original_data"
designFp <- "../../data/original_data/hela_design.tsv"
dataFp <- "../../data/original_data/hela.tsv"

normMatrixPath <- paste(outDir, "../../data/original_data/hela/RT-VSN-normalized.txt", sep="/")
normalyzerDE("hela",
             comparisons=c("2-5"),
             designPath=designFp,
             dataPath=normMatrixPath,
             outputDir=outDir,
             condCol="group")

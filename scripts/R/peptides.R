library('Peptides')



batch_info = read.csv('../../data/original_data/plasma1/plasma_data.csv')

batch_info$Aliphatic = aIndex(batch_info$Sequence)

batch_info$Istablity = instaIndex(batch_info$Sequence)

batch_info$Boman = boman(batch_info$Seq)

batch_info$Mass = mw(batch_info$Seq, monoisotopic = FALSE)
aaComposition = data.frame(Tiny=numeric(), Small=numeric(), Aliphatic=numeric(),  Aromatic=numeric(), NonPolar=numeric(), Polar=numeric(), Charged=numeric(), Basic=numeric(), Acidic=numeric() )
for(s in batch_info$Seq)
  aaComposition = rbind(aaComposition, data.frame(t(aaComp(s)[[1]][,2])))
names(aaComposition)[3] = 'Alphatic-aa'

fasgai = data.frame(F1=numeric(), F2=numeric(), F3=numeric(),  F4=numeric(), F5=numeric(), F6=numeric())
for(s in batch_info$Seq)
  fasgai = rbind(fasgai, data.frame(t(fasgaiVectors(s)[[1]])))
colnames(fasgai) = c('Hydrophobicity', 'Alpha', 'Bulk', 'Compositional', 'Local flexibility',  'Electronic properties')

info = cbind(batch_info, aaComposition, fasgai)

write.csv(info, file = '../../data/original_data/plasma1/plasma_trainSet.csv',row.names = F)


library("quantmod")
library(PerformanceAnalytics)
library(tseries)
library(fitdistrplus)
library(stargazer)
library(car)
library(ggfortify)
library(MASS)
library(TTR)
library( ggplot2)
library( GGally)
library(psych)


#descarga serie de tiempo: Define el horizonte temporal

getSymbols.yahoo('AMZN',env=globalenv(),return.class="xts",
                 from='2020-08-30',to='2021-08-30',
                 periodicity='daily')
getSymbols.yahoo('^GSPC',env=globalenv(),return.class="xts",
                 from='2020-08-30',to='2021-08-30',
                 periodicity='daily')

#Especifica el campo de la serie de datos. En este caso fueron los precios ajustados.

AMZN <- AMZN[,"AMZN.Adjusted"]
GSPC <- GSPC[,"GSPC.Adjusted"]
datos<- merge(GSPC, AMZN)
ggpairs(datos)
ggpairs(datos,lower = list(continuous = "smooth"),
        diag = list(continuous = "barDiag"), axisLabels = "none")

#Calcula los retornos de ambas varaibles


AMZNrt<- diff(log(AMZN))
DGSPC <- diff(log(GSPC))


#define que estas trabajando con una serie de tiempo ts
FB<- ts(KO,frequency=12)
FBS<- ts(AMZNrt,frequency=12)
DGSPCS<- ts(DGSPC,frequency=12)
retdata<- merge(DGSPC, AMZNrt)
ggpairs(retdata)
ggpairs(retdata,lower = list(continuous = "smooth"),
        diag = list(continuous = "barDiag"), axisLabels = "none")


#Grafica ambas variables en su forma original y en sus retornos

chart_Series(AMZNrt)
chart_Series(DGSPC)

#Estima la regresi?n


regresion <- lm(FBS ~ DGSPCS)
summary(regresion)

#Normalidad en los residuos

jarque.bera.test(residuals(regresion))

sresid <- stdres(regresion)
hist(sresid, freq=FALSE, 
     main="Distribution of Studentized Residuals")
xfit<-seq(min(sresid),max(sresid),length=40)
yfit<-dnorm(xfit)
lines(xfit, yfit)

# Prueba de heterocedasticidad breusch pagan test

library(lmtest)
bptest(regresion)

# Independencia de los errores durbin watson test

dwtest(regresion)
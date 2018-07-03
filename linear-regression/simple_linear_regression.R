#Simple Linear Regression

dataset = read.csv('Salary_Data.csv')

#Splitting the dataser into the training ser and Test set
#install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

#Feature Scaling
#training_set[, 2:3] = scale(training_set[, 2:3])
#test_set[, 2:3] = scale(test_set[, 2:3])

#Fitting Simple Linear Regression to the Training set
regressor = lm(formula = Salary ~ YearsExperience, data = training_set)

#Predicting the Test set Results
y_pred = predict(regressor, newdata = test_set) 

#Visualising the Training set results
#install.packages('ggplot2')
library(ggplot2)
ggplot() + 
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary), 
             color = 'red') +
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata =  training_set)),
            color = 'blue') +
  ggtitle('Salary vs Experience (Training set') +
  xlab('Years of experience') +
  ylab('Salary')

ggplot() + 
  geom_point(aes(x = test_set$YearsExperience, y = test_set$Salary), 
             color = 'red') +
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata =  training_set)),
            color = 'blue') +
  ggtitle('Salary vs Experience (Training set') +
  xlab('Years of experience') +
  ylab('Salary')

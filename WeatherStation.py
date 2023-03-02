class Subject:
    # Both of the following two methods take an
    # observer as an argument; that is, the observer
    # to be registered ore removed.
    def registerObserver(observer):
        pass
    def removeObserver(observer):
        pass
    
    # This method is called to notify all observers
    # when the Subject's state (measurements) has changed.
    def notifyObservers():
        pass
    
# The observer class is implemented by all observers,
# so they all have to implemented the update() method. Here
# we're following Mary and Sue's lead and 
# passing the measurements to the observers.
class Observer:
    def update(self, temp, humidity, pressure):
        pass


# WeatherData now implements the subject interface.
class WeatherData(Subject):
    
    def __init__(self):        
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0
    
    
    def registerObserver(self, observer):
        # When an observer registers, we just 
        # add it to the end of the list.
        self.observers.append(observer)
        
    def removeObserver(self, observer):
        # When an observer wants to un-register,
        # we just take it off the list.
        self.observers.remove(observer)
    
    def notifyObservers(self):
        # We notify the observers when we get updated measurements 
        # from the Weather Station.
        for ob in self.observers:
            ob.update(self.temperature, self.humidity, self.pressure)
    
    def measurementsChanged(self):
            self.notifyObservers()
        
    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        
        self.measurementsChanged()
    
    # other WeatherData methods here.


class CurrentConditionsDisplay(Observer):
    
    def __init__(self, weatherData):        
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0
        
        self.weatherData = weatherData # save the ref in an attribute.
        weatherData.registerObserver(self) # register the observer 
                                        # so it gets data updates.
    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()
        
    def display(self):
        print("Current conditions:", self.temperature, 
            "F degrees and", self.humidity,"[%] humidity",
            "and pressure", self.pressure)
        
# TODO: implement StatisticsDisplay class and ForecastDisplay class.
class StatisticsDisplay(Observer):
    
    def __init__(self, weatherData):        
        self.temperature_list = []
        self.humidity_list = []
        self.pressure_list = []
        
        self.weatherData = weatherData # save the ref in an attribute.
        weatherData.registerObserver(self) # register the observer 
                                        # so it gets data updates.
    
    def update(self, temperature, humidity, pressure):
        self.temperature_list.append(temperature)
        self.humidity_list.append(humidity)
        self.pressure_list.append(pressure)
        self.display()
    
    def display(self):
        avg_temp = sum(self.temperature_list) / len(self.temperature_list)
        avg_humidity = sum(self.humidity_list) / len(self.humidity_list)
        avg_pressure = sum(self.pressure_list) / len(self.pressure_list)
        min_temp = min(self.temperature_list)
        min_humidity = min(self.humidity_list)
        min_pressure = min(self.pressure_list)
        max_temp = max(self.temperature_list)
        max_humidity = max(self.humidity_list)
        max_pressure = max(self.pressure_list)
        
        print("Avg/Min/Max temperature:", round(avg_temp, 1), "/", min_temp, "/", max_temp)
        print("Avg/Min/Max humidity:", round(avg_humidity, 1), "/", min_humidity, "/", max_humidity)
        print("Avg/Min/Max pressure:", round(avg_pressure, 1), "/", min_pressure, "/", max_pressure)


class ForecastDisplay(Observer):
    
    def __init__(self, weatherData):        
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0
        
        self.weatherData = weatherData # save the ref in an attribute.
        weatherData.registerObserver(self) # register the observer 
                                        # so it gets data updates.
    
    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()
    
    def display(self):
        forecast_temp = self.temperature + 0.11 * self.humidity + 0.2 * self.pressure
        forecast_humidity = self.humidity - 0.9 * self.humidity
        forecast_pressure = self.pressure + 0.1 * self.temperature - 0.21 * self.pressure
        
        print("Forecast temperature:", round(forecast_temp, 1))
        print("Forecast humidity:", round(forecast_humidity, 1))
        print("Forecast pressure:", round(forecast_pressure, 1))


class WeatherStation:
    def main(self):
        weather_data = WeatherData()
        current_display = CurrentConditionsDisplay(weather_data)
        statistics_display = StatisticsDisplay(weather_data)
        forecast_display = ForecastDisplay(weather_data)
        
        weather_data.setMeasurements(80, 65, 30.4)
        weather_data.setMeasurements(82, 70, 29.2)
        weather_data.setMeasurements(78, 90, 29.2)
        
        weather_data.removeObserver(current_display)
        weather_data.removeObserver(statistics_display)
        weather_data.removeObserver(forecast_display)
        weather_data.setMeasurements(120, 100, 1000)

if __name__ == "__main__":
    w = WeatherStation()
    w.main()
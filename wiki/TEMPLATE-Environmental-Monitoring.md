# 🌡️ Environmental Monitoring Template

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/templates/TEMPLATE_environmental_monitoring.ipynb)

> **Real-time environmental data collection, analysis, and alerts for plant monitoring**

---

## 📋 Overview

The **Environmental Monitoring Template** provides a comprehensive framework for tracking environmental conditions critical to plant health. Monitor temperature, humidity, light levels, soil moisture, and more with automated data logging, visualization, and alerting systems.

### Perfect For
- 🌱 **Greenhouse management** — Monitor growing conditions
- 🏡 **Garden monitoring** — Track outdoor environments
- 🔬 **Research projects** — Collect experimental data
- 📊 **Climate studies** — Long-term environmental tracking
- ⚠️ **Alert systems** — Automated notifications

---

## 🎯 Use Cases

### Greenhouse & Indoor Growing
- ✅ **Climate control** — Monitor temperature and humidity
- ✅ **Light optimization** — Track PAR levels and photoperiod
- ✅ **VPD monitoring** — Optimize vapor pressure deficit
- ✅ **CO₂ tracking** — Monitor enrichment systems
- ✅ **Automated alerts** — Get notified of issues

### Outdoor Gardens
- ✅ **Weather monitoring** — Track local conditions
- ✅ **Soil moisture** — Optimize irrigation
- ✅ **Frost alerts** — Protect sensitive plants
- ✅ **Growing degree days** — Track heat accumulation
- ✅ **Rainfall tracking** — Monitor precipitation

### Research Applications
- ✅ **Controlled experiments** — Document conditions
- ✅ **Climate chambers** — Monitor experimental setups
- ✅ **Field studies** — Remote data collection
- ✅ **Phenology tracking** — Link environment to growth
- ✅ **Data validation** — Quality control

---

## ⭐ Key Features

### Multi-Sensor Integration

**Supported sensor types:**
```python
class EnvironmentalMonitor:
    """
    Unified interface for environmental sensors.
    
    Supported sensors:
        - Temperature (DHT22, DS18B20, BME280)
        - Humidity (DHT22, BME280)
        - Light (BH1750, TSL2561)
        - Soil moisture (capacitive, resistive)
        - CO₂ (MH-Z19, SCD30)
        - Air pressure (BME280, BMP280)
    """
    
    def read_temperature(self) -> float:
        """Get temperature in Celsius."""
        pass
    
    def read_humidity(self) -> float:
        """Get relative humidity (%)."""
        pass
    
    def read_light(self) -> float:
        """Get light intensity (lux)."""
        pass
    
    def read_soil_moisture(self) -> float:
        """Get soil moisture (%)."""
        pass
    
    def calculate_vpd(self, temp: float, rh: float) -> float:
        """
        Calculate Vapor Pressure Deficit.
        
        VPD = (1 - RH/100) * SVP(T)
        where SVP is saturated vapor pressure
        """
        svp = 0.6108 * np.exp((17.27 * temp) / (temp + 237.3))
        vpd = (1 - rh / 100) * svp
        return vpd
```

### Real-Time Data Logging

**Automated data collection:**
```python
import pandas as pd
from datetime import datetime
import time

def start_monitoring(
    interval_seconds: int = 60,
    duration_hours: int = 24
) -> pd.DataFrame:
    """
    Continuous environmental monitoring.
    
    Args:
        interval_seconds: Time between readings
        duration_hours: How long to monitor
    
    Returns:
        DataFrame with all readings
    """
    data = []
    end_time = time.time() + (duration_hours * 3600)
    
    while time.time() < end_time:
        reading = {
            'timestamp': datetime.now(),
            'temperature': read_temperature(),
            'humidity': read_humidity(),
            'light': read_light(),
            'soil_moisture': read_soil_moisture()
        }
        
        # Calculate derived metrics
        reading['vpd'] = calculate_vpd(
            reading['temperature'],
            reading['humidity']
        )
        
        # Add to dataset
        data.append(reading)
        
        # Display current reading
        print(f"{reading['timestamp']}: "
              f"Temp: {reading['temperature']:.1f}°C, "
              f"RH: {reading['humidity']:.1f}%, "
              f"VPD: {reading['vpd']:.2f} kPa")
        
        # Wait for next reading
        time.sleep(interval_seconds)
    
    return pd.DataFrame(data)
```

### Automated Alerts

**Condition-based notifications:**
```python
class AlertSystem:
    """
    Monitor conditions and send alerts.
    """
    
    def __init__(self):
        self.thresholds = {
            'temperature_min': 15.0,
            'temperature_max': 30.0,
            'humidity_min': 40.0,
            'humidity_max': 80.0,
            'soil_moisture_min': 20.0,
            'vpd_max': 1.5
        }
        
    def check_conditions(self, reading: Dict) -> List[str]:
        """
        Check if any thresholds are exceeded.
        
        Returns:
            List of alert messages
        """
        alerts = []
        
        # Temperature alerts
        if reading['temperature'] < self.thresholds['temperature_min']:
            alerts.append(
                f"⚠️ LOW TEMPERATURE: {reading['temperature']:.1f}°C "
                f"(min: {self.thresholds['temperature_min']}°C)"
            )
        elif reading['temperature'] > self.thresholds['temperature_max']:
            alerts.append(
                f"🔥 HIGH TEMPERATURE: {reading['temperature']:.1f}°C "
                f"(max: {self.thresholds['temperature_max']}°C)"
            )
        
        # Humidity alerts
        if reading['humidity'] < self.thresholds['humidity_min']:
            alerts.append(
                f"💧 LOW HUMIDITY: {reading['humidity']:.1f}% "
                f"(min: {self.thresholds['humidity_min']}%)"
            )
        elif reading['humidity'] > self.thresholds['humidity_max']:
            alerts.append(
                f"💦 HIGH HUMIDITY: {reading['humidity']:.1f}% "
                f"(max: {self.thresholds['humidity_max']}%)"
            )
        
        # VPD alert
        if reading['vpd'] > self.thresholds['vpd_max']:
            alerts.append(
                f"🌿 HIGH VPD: {reading['vpd']:.2f} kPa "
                f"(max: {self.thresholds['vpd_max']} kPa) - Plants may be stressed"
            )
        
        return alerts
    
    def send_notification(self, message: str) -> None:
        """Send alert via email or SMS."""
        # Email integration
        # SMS integration
        print(f"📧 ALERT: {message}")
```

### Advanced Visualizations

**Real-time dashboard:**
```python
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def create_live_dashboard(monitor: EnvironmentalMonitor) -> None:
    """
    Create live updating dashboard.
    """
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    
    # Initialize data lists
    timestamps = []
    temperatures = []
    humidities = []
    vpds = []
    lights = []
    
    def update(frame):
        # Read sensors
        temp = monitor.read_temperature()
        humidity = monitor.read_humidity()
        light = monitor.read_light()
        vpd = monitor.calculate_vpd(temp, humidity)
        
        # Append data
        timestamps.append(datetime.now())
        temperatures.append(temp)
        humidities.append(humidity)
        vpds.append(vpd)
        lights.append(light)
        
        # Keep last 100 readings
        if len(timestamps) > 100:
            timestamps.pop(0)
            temperatures.pop(0)
            humidities.pop(0)
            vpds.pop(0)
            lights.pop(0)
        
        # Clear axes
        for ax in axes.flat:
            ax.clear()
        
        # Plot temperature
        axes[0, 0].plot(timestamps, temperatures, 'r-')
        axes[0, 0].set_title('Temperature (°C)')
        axes[0, 0].axhline(y=20, color='g', linestyle='--', alpha=0.3)
        axes[0, 0].axhline(y=25, color='r', linestyle='--', alpha=0.3)
        
        # Plot humidity
        axes[0, 1].plot(timestamps, humidities, 'b-')
        axes[0, 1].set_title('Humidity (%)')
        axes[0, 1].axhline(y=60, color='g', linestyle='--', alpha=0.3)
        
        # Plot VPD
        axes[1, 0].plot(timestamps, vpds, 'g-')
        axes[1, 0].set_title('VPD (kPa)')
        axes[1, 0].axhline(y=0.8, color='g', linestyle='--', alpha=0.3)
        axes[1, 0].axhline(y=1.2, color='r', linestyle='--', alpha=0.3)
        
        # Plot light
        axes[1, 1].plot(timestamps, lights, 'y-')
        axes[1, 1].set_title('Light (lux)')
        
        plt.tight_layout()
    
    anim = FuncAnimation(fig, update, interval=1000)
    plt.show()
```

### Data Export & Reporting

**Automated reports:**
```python
def generate_daily_report(df: pd.DataFrame) -> str:
    """
    Generate daily summary report.
    
    Returns:
        Formatted report string
    """
    report = f"""
    📊 DAILY ENVIRONMENTAL REPORT
    ============================
    Date: {df['timestamp'].iloc[-1].date()}
    Duration: {len(df)} readings
    
    🌡️ TEMPERATURE
    - Average: {df['temperature'].mean():.1f}°C
    - Min: {df['temperature'].min():.1f}°C at {df.loc[df['temperature'].idxmin(), 'timestamp'].strftime('%H:%M')}
    - Max: {df['temperature'].max():.1f}°C at {df.loc[df['temperature'].idxmax(), 'timestamp'].strftime('%H:%M')}
    - Std Dev: {df['temperature'].std():.1f}°C
    
    💧 HUMIDITY
    - Average: {df['humidity'].mean():.1f}%
    - Min: {df['humidity'].min():.1f}%
    - Max: {df['humidity'].max():.1f}%
    
    🌿 VPD
    - Average: {df['vpd'].mean():.2f} kPa
    - Min: {df['vpd'].min():.2f} kPa
    - Max: {df['vpd'].max():.2f} kPa
    - Time in optimal range (0.8-1.2 kPa): {((df['vpd'] >= 0.8) & (df['vpd'] <= 1.2)).sum() / len(df) * 100:.1f}%
    
    ☀️ LIGHT
    - Average: {df['light'].mean():.0f} lux
    - Daily Light Integral: {calculate_dli(df):.1f} mol/m²/day
    
    ⚠️ ALERTS
    - Temperature out of range: {((df['temperature'] < 15) | (df['temperature'] > 30)).sum()} times
    - Humidity out of range: {((df['humidity'] < 40) | (df['humidity'] > 80)).sum()} times
    """
    
    return report
```

---

## 📦 What's Included

1. **Sensor Integration** — DHT22, BME280, soil sensors
2. **Data Logging** — Continuous monitoring
3. **Alert System** — Threshold-based notifications
4. **Live Dashboard** — Real-time visualization
5. **Data Export** — CSV, JSON formats
6. **Daily Reports** — Automated summaries
7. **VPD Calculator** — Optimize growing conditions
8. **Growing Degree Days** — Heat accumulation tracking

---

## 🚀 Quick Start

```python
# 1. Initialize monitor
monitor = EnvironmentalMonitor()

# 2. Set up alerts
alert_system = AlertSystem()
alert_system.thresholds['temperature_max'] = 28.0

# 3. Start monitoring
data = start_monitoring(interval_seconds=300, duration_hours=24)

# 4. Generate report
report = generate_daily_report(data)
print(report)

# 5. Export data
data.to_csv('environmental_log.csv', index=False)
```

---

## 📚 Related Resources

- [Greenhouse Data Visualization](Greenhouse-Data-Visualization)
- [Regional Finnish Weather Analysis](Regional-Finnish-Weather-Analysis)

---

## 📄 License

MIT License — Free to use, modify, and distribute

[← Back to Templates](Home#-templates) | [View on GitHub](https://github.com/outobecca/botanical-colabs/blob/main/notebooks/templates/TEMPLATE_environmental_monitoring.ipynb)

# TrueSight Pulse Sine Wave Meter Plugin
Example plugin that outputs multiple measurements sources that are Sine Waves with optional Gaussian noise add to the measurement.

### Prerequisites

|     OS    | Linux | Windows | SmartOS | OS X |
|:----------|:-----:|:-------:|:-------:|:----:|
| Supported |   v   |    v    |    v    |  v   |

* Requires Python 2.7.10 or later

### Plugin Setup

None

### Plugin Configuration Fields

|Field Name   | Description                                                                                          |
|:------------|:-----------------------------------------------------------------------------------------------------|
| Name        | Name of the sine wave                                                                                |
| Amplititude | Unitless value of the max value of the sine save                                                     |        
| Frequency   | Frequency in hertz of the sine wave                                                                  |
| Noise       | Enable/Disable noise generation to the sine wave                                                     |
| Mu          | Mean value of generated noise                                                                        |
| Sigma       | Standard deviation of generated noise                                                                |
| Sample Rate | How often (in milliseconds) to collect values from the sine wave.                                    |
| Debug Level | Sets the level of debug output. One of the following: CRITICALi, ERROR, WARNING, INFO, DEBUG, NOTSET |

### Metrics Collected

|Metric Name          |Description                         |
|:--------------------|:-----------------------------------|
| SINE\_WAVE\_AMPLITUDE | Amplitude of the measured Sine Wave|

### Dashboards

- Sine Wave

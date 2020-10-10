# **Queen Alia International Airport - Openscope**

## **About Queen Alia International Airport**
Located approximately 25 kilometers south of the capital Amman, Queen Alia International Airport is the main international airport serving the Hashemite Kingdom of Jordan. It is one of 3 airports which are: *Amman - Marka Civil Airport*, and *Aqaba - King Hussein International Airport*.

## **Statistics**
[Insert some statistics here]

## **Civil Aviation Regulatory Commission (CARC)**
The Civil Aviation Regulatory Commission of Jordan is the air navigation services provider for all airports in Jordan.

## **Positions**

| Callsign | Frequency |
|:----------|:----------:|
| Amman Control | 128.500 MHz |
| Amman Approach | 128.900 MHz |
| Queen Alia Tower | 119.800 MHz |
| Queen Alia Ground | 121.900 MHz |

## **Sectors Available on Openscope**
For simulation purposes, the only available sector is *Amman Approach*. Other sectors are included in the definitions but not simulated.

## **Procedures**
### **Arrivals**
Queen Alia International Airport is rarely busy. Most of the time, flights are given direct routes to one of the four RNAV fixes around the airport: `RESOS`, `ORDUN`, `ASPAL`, `LOTES`.  
The main purpose is the transition to the ILS in shortest distance. Occasionally, controllers use vectors for more precise control of the airspace.  

Example:  
**RJA23Q**: *Amman Approach, RJA23Q, One-One-Thousand at `OSAMA`.*  

**Amman Approach**: *RJA23Q, Amman Approach, identified. Leave `OSAMA` heading 090. Descend 6,000 ft. Queen Alia QNH 1005 hPa.*  

#### **Special Case**
Arrivals from the east on the published `GENEX` and `ELOXI` STARs for RWY 26L/R are often high on their descent profile due to the restriction published. In real life, these restrictions are ignored to ensure a smooth transition to the ILS.

### **Departures**
Queen Alia International Airport SIDs are straight forward. A direct to the exit point is often given to all flights. There are two exceptions to this case:
#### **West Departures from RWY 26L/R**
1. Due to the proximity to the western border, flights departing Queen Alia International Airport and overflying `LLLL` airspace are bound by a 12,000 ft. restriction at exit point `MOUAB` until two-way communication has been established by the appropriate `LLLL` air traffic service facility.
2. Flights departing Queen Alia International Airport and terminating in `LLLL` airspace are to use the `OSAMA` departure procedure. The restriction at `OSAMA` is 8,000 ft.  

#### **East Departures**
Traffic departing Queen Alia International Airport towards the east entering `OEJD` airspace are often given a direct to the `GRY` VOR. This is a mutual agreement with `OEJD` FIR.

## **Separation**
All flights in `OJAC` airspace must be separated with the radar separation minima of **5nm** laterlally, **1,000 ft.** vertically, and with the published *wake turbulence separation minima* longitudinally.

### **Separation of Landing Traffic**
Since parallel approaches are not supported in Queen Alia International Airport, a **5nm** separation minima shall exist between consecutive arrivals on any runway.
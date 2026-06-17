# 🏆 Predicción completa del Mundial 2026 — los 104 partidos

Generado con el modelo de este repositorio: regresores XGBoost (Tweedie) de goles + clasificador 1X2 XGBoost calibrado (isotónico), predicción a sede neutral con "efecto espejo", temperatura `T=0.27` en grupos y `T=0.5` en eliminatorias, y simulación de **Monte Carlo de 10.000 mundiales** para las probabilidades por selección.

> ⚠️ Predicción generada el 12-jun-2026, con los datos del repo (anteriores al torneo). La asignación de mejores terceros al cuadro usa la simplificación del notebook (ranking 1º-8º a huecos fijos), no la tabla oficial de la FIFA.

## Resumen

| | |
|---|---|
| 🥇 **Campeón predicho** | **🇫🇷 Francia** |
| 🥈 Subcampeón | 🇦🇷 Argentina |
| 🥉 Tercer puesto | 🇪🇸 España |

### Probabilidades de ser campeón (Top 10, Monte Carlo)

| # | Selección | Campeón | Final | Semis | Cuartos |
|---|---|---|---|---|---|
| 1 | 🇫🇷 Francia | **27.9%** | 38.8% | 59.8% | 70.0% |
| 2 | 🇪🇸 España | **20.2%** | 32.5% | 54.7% | 64.2% |
| 3 | 🇦🇷 Argentina | **17.6%** | 35.1% | 55.1% | 73.2% |
| 4 | 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra | **17.4%** | 38.2% | 63.5% | 81.0% |
| 5 | 🇩🇪 Alemania | **4.1%** | 8.5% | 17.8% | 29.9% |
| 6 | 🇵🇹 Portugal | **3.9%** | 13.1% | 32.0% | 69.5% |
| 7 | 🇧🇪 Bélgica | **3.0%** | 8.1% | 25.4% | 78.9% |
| 8 | 🇳🇱 Países Bajos | **2.2%** | 6.4% | 16.2% | 46.6% |
| 9 | 🇭🇷 Croacia | **0.9%** | 3.5% | 11.9% | 23.8% |
| 10 | 🇧🇷 Brasil | **0.9%** | 4.6% | 12.6% | 40.1% |

## Fase de grupos — 72 partidos

Marcador = marcador exacto más probable según los goles esperados del modelo, condicionado al resultado 1X2 más probable.

### Grupo A

| Fecha | Partido | Pred. | P(1) | P(X) | P(2) |
|---|---|:-:|--:|--:|--:|
| 06-11 | 🇲🇽 México – 🇿🇦 Sudáfrica | **1-0** | 85% | 12% | 4% |
| 06-11 | 🇰🇷 Corea del Sur – 🇨🇿 República Checa | **1-0** | 68% | 24% | 8% |
| 06-18 | 🇨🇿 República Checa – 🇿🇦 Sudáfrica | **0-1** | 39% | 20% | 41% |
| 06-18 | 🇲🇽 México – 🇰🇷 Corea del Sur | **1-0** | 60% | 32% | 9% |
| 06-24 | 🇿🇦 Sudáfrica – 🇰🇷 Corea del Sur | **0-1** | 4% | 32% | 64% |
| 06-24 | 🇨🇿 República Checa – 🇲🇽 México | **0-1** | 3% | 9% | 88% |

| Pos | Equipo | Pts | DG (xG) |
|---|---|--:|--:|
| 1 | 🇲🇽 México ✅ | 9 | +2.85 |
| 2 | 🇰🇷 Corea del Sur ✅ | 6 | +1.23 |
| 3 | 🇿🇦 Sudáfrica 🟡 | 3 | -2.50 |
| 4 | 🇨🇿 República Checa | 0 | -1.58 |

### Grupo B

| Fecha | Partido | Pred. | P(1) | P(X) | P(2) |
|---|---|:-:|--:|--:|--:|
| 06-12 | 🇨🇦 Canadá – 🇧🇦 Bosnia-Herzegovina | **1-0** | 77% | 20% | 3% |
| 06-13 | 🇶🇦 Catar – 🇨🇭 Suiza | **0-1** | 1% | 8% | 91% |
| 06-18 | 🇨🇭 Suiza – 🇧🇦 Bosnia-Herzegovina | **2-1** | 74% | 16% | 11% |
| 06-18 | 🇨🇦 Canadá – 🇶🇦 Catar | **1-0** | 68% | 29% | 3% |
| 06-24 | 🇧🇦 Bosnia-Herzegovina – 🇶🇦 Catar | **1-0** | 39% | 28% | 33% |
| 06-24 | 🇨🇭 Suiza – 🇨🇦 Canadá | **1-0** | 35% | 31% | 34% |

| Pos | Equipo | Pts | DG (xG) |
|---|---|--:|--:|
| 1 | 🇨🇭 Suiza ✅ | 7 | +0.85 |
| 2 | 🇨🇦 Canadá ✅ | 4 | +0.41 |
| 3 | 🇧🇦 Bosnia-Herzegovina 🟡 | 4 | -0.45 |
| 4 | 🇶🇦 Catar | 1 | -0.81 |

### Grupo C

| Fecha | Partido | Pred. | P(1) | P(X) | P(2) |
|---|---|:-:|--:|--:|--:|
| 06-13 | 🇧🇷 Brasil – 🇲🇦 Marruecos | **0-1** | 39% | 18% | 42% |
| 06-13 | 🇭🇹 Haití – 🏴󠁧󠁢󠁳󠁣󠁴󠁿 Escocia | **0-1** | 4% | 7% | 89% |
| 06-19 | 🏴󠁧󠁢󠁳󠁣󠁴󠁿 Escocia – 🇲🇦 Marruecos | **0-1** | 3% | 10% | 87% |
| 06-19 | 🇧🇷 Brasil – 🇭🇹 Haití | **2-0** | 99% | 1% | 0% |
| 06-24 | 🇲🇦 Marruecos – 🇭🇹 Haití | **2-0** | 97% | 2% | 0% |
| 06-24 | 🏴󠁧󠁢󠁳󠁣󠁴󠁿 Escocia – 🇧🇷 Brasil | **1-2** | 1% | 7% | 92% |

| Pos | Equipo | Pts | DG (xG) |
|---|---|--:|--:|
| 1 | 🇧🇷 Brasil ✅ | 7 | +2.89 |
| 2 | 🇲🇦 Marruecos ✅ | 7 | +2.64 |
| 3 | 🏴󠁧󠁢󠁳󠁣󠁴󠁿 Escocia 🟡 | 3 | -0.82 |
| 4 | 🇭🇹 Haití | 0 | -4.71 |

### Grupo D

| Fecha | Partido | Pred. | P(1) | P(X) | P(2) |
|---|---|:-:|--:|--:|--:|
| 06-12 | 🇺🇸 EE. UU. – 🇵🇾 Paraguay | **1-0** | 63% | 28% | 10% |
| 06-13 | 🇦🇺 Australia – 🇹🇷 Turquía | **0-1** | 26% | 20% | 54% |
| 06-19 | 🇺🇸 EE. UU. – 🇦🇺 Australia | **1-0** | 54% | 24% | 22% |
| 06-19 | 🇹🇷 Turquía – 🇵🇾 Paraguay | **1-0** | 84% | 11% | 5% |
| 06-25 | 🇵🇾 Paraguay – 🇦🇺 Australia | **0-1** | 8% | 17% | 76% |
| 06-25 | 🇹🇷 Turquía – 🇺🇸 EE. UU. | **1-0** | 48% | 26% | 26% |

| Pos | Equipo | Pts | DG (xG) |
|---|---|--:|--:|
| 1 | 🇺🇸 EE. UU. ✅ | 6 | +3.10 |
| 2 | 🇦🇺 Australia ✅ | 6 | +2.04 |
| 3 | 🇹🇷 Turquía 🟡 | 6 | -1.05 |
| 4 | 🇵🇾 Paraguay | 0 | -4.09 |

### Grupo E

| Fecha | Partido | Pred. | P(1) | P(X) | P(2) |
|---|---|:-:|--:|--:|--:|
| 06-14 | 🇩🇪 Alemania – 🇨🇼 Curazao | **2-0** | 99% | 1% | 0% |
| 06-14 | 🇨🇮 Costa de Marfil – 🇪🇨 Ecuador | **1-0** | 58% | 23% | 19% |
| 06-20 | 🇩🇪 Alemania – 🇨🇮 Costa de Marfil | **1-0** | 89% | 9% | 2% |
| 06-20 | 🇪🇨 Ecuador – 🇨🇼 Curazao | **1-0** | 95% | 4% | 1% |
| 06-25 | 🇨🇼 Curazao – 🇨🇮 Costa de Marfil | **0-1** | 0% | 4% | 95% |
| 06-25 | 🇪🇨 Ecuador – 🇩🇪 Alemania | **0-1** | 1% | 8% | 91% |

| Pos | Equipo | Pts | DG (xG) |
|---|---|--:|--:|
| 1 | 🇩🇪 Alemania ✅ | 9 | +7.57 |
| 2 | 🇨🇮 Costa de Marfil ✅ | 6 | +1.67 |
| 3 | 🇪🇨 Ecuador 🟡 | 3 | -0.84 |
| 4 | 🇨🇼 Curazao | 0 | -8.40 |

### Grupo F

| Fecha | Partido | Pred. | P(1) | P(X) | P(2) |
|---|---|:-:|--:|--:|--:|
| 06-14 | 🇳🇱 Países Bajos – 🇯🇵 Japón | **1-0** | 63% | 29% | 9% |
| 06-14 | 🇸🇪 Suecia – 🇹🇳 Túnez | **1-0** | 46% | 32% | 23% |
| 06-20 | 🇳🇱 Países Bajos – 🇸🇪 Suecia | **2-1** | 90% | 8% | 2% |
| 06-20 | 🇹🇳 Túnez – 🇯🇵 Japón | **0-1** | 2% | 3% | 95% |
| 06-25 | 🇯🇵 Japón – 🇸🇪 Suecia | **1-0** | 92% | 8% | 1% |
| 06-25 | 🇹🇳 Túnez – 🇳🇱 Países Bajos | **0-1** | 0% | 5% | 95% |

| Pos | Equipo | Pts | DG (xG) |
|---|---|--:|--:|
| 1 | 🇳🇱 Países Bajos ✅ | 7 | +1.81 |
| 2 | 🇯🇵 Japón ✅ | 7 | +1.26 |
| 3 | 🇸🇪 Suecia 🟡 | 3 | +2.45 |
| 4 | 🇹🇳 Túnez | 0 | -5.52 |

### Grupo G

| Fecha | Partido | Pred. | P(1) | P(X) | P(2) |
|---|---|:-:|--:|--:|--:|
| 06-15 | 🇧🇪 Bélgica – 🇪🇬 Egipto | **1-0** | 94% | 5% | 1% |
| 06-15 | 🇮🇷 Irán – 🇳🇿 Nueva Zelanda | **1-0** | 91% | 8% | 1% |
| 06-21 | 🇧🇪 Bélgica – 🇮🇷 Irán | **1-0** | 76% | 21% | 3% |
| 06-21 | 🇳🇿 Nueva Zelanda – 🇪🇬 Egipto | **0-1** | 1% | 8% | 91% |
| 06-26 | 🇳🇿 Nueva Zelanda – 🇧🇪 Bélgica | **0-2** | 0% | 2% | 98% |
| 06-26 | 🇪🇬 Egipto – 🇮🇷 Irán | **0-1** | 8% | 21% | 72% |

| Pos | Equipo | Pts | DG (xG) |
|---|---|--:|--:|
| 1 | 🇧🇪 Bélgica ✅ | 7 | +2.20 |
| 2 | 🇪🇬 Egipto ✅ | 4 | +0.30 |
| 3 | 🇮🇷 Irán 🟡 | 4 | -0.14 |
| 4 | 🇳🇿 Nueva Zelanda | 1 | -2.36 |

### Grupo H

| Fecha | Partido | Pred. | P(1) | P(X) | P(2) |
|---|---|:-:|--:|--:|--:|
| 06-15 | 🇪🇸 España – 🇨🇻 Cabo Verde | **2-0** | 92% | 7% | 0% |
| 06-15 | 🇸🇦 Arabia Saudí – 🇺🇾 Uruguay | **0-2** | 0% | 4% | 96% |
| 06-21 | 🇪🇸 España – 🇸🇦 Arabia Saudí | **2-0** | 98% | 2% | 0% |
| 06-21 | 🇺🇾 Uruguay – 🇨🇻 Cabo Verde | **1-0** | 85% | 12% | 3% |
| 06-26 | 🇺🇾 Uruguay – 🇪🇸 España | **0-1** | 1% | 14% | 84% |
| 06-26 | 🇨🇻 Cabo Verde – 🇸🇦 Arabia Saudí | **1-0** | 64% | 19% | 17% |

| Pos | Equipo | Pts | DG (xG) |
|---|---|--:|--:|
| 1 | 🇪🇸 España ✅ | 7 | +3.11 |
| 2 | 🇺🇾 Uruguay ✅ | 4 | -0.02 |
| 3 | 🇨🇻 Cabo Verde 🟡 | 4 | -0.58 |
| 4 | 🇸🇦 Arabia Saudí | 1 | -2.51 |

### Grupo I

| Fecha | Partido | Pred. | P(1) | P(X) | P(2) |
|---|---|:-:|--:|--:|--:|
| 06-16 | 🇫🇷 Francia – 🇸🇳 Senegal | **1-0** | 85% | 12% | 2% |
| 06-16 | 🇮🇶 Irak – 🇳🇴 Noruega | **0-1** | 1% | 4% | 95% |
| 06-22 | 🇫🇷 Francia – 🇮🇶 Irak | **2-0** | 99% | 1% | 0% |
| 06-22 | 🇳🇴 Noruega – 🇸🇳 Senegal | **0-1** | 16% | 27% | 57% |
| 06-26 | 🇳🇴 Noruega – 🇫🇷 Francia | **0-2** | 1% | 5% | 94% |
| 06-26 | 🇸🇳 Senegal – 🇮🇶 Irak | **1-0** | 96% | 3% | 1% |

| Pos | Equipo | Pts | DG (xG) |
|---|---|--:|--:|
| 1 | 🇫🇷 Francia ✅ | 9 | +3.93 |
| 2 | 🇸🇳 Senegal ✅ | 6 | +1.09 |
| 3 | 🇳🇴 Noruega 🟡 | 3 | -0.97 |
| 4 | 🇮🇶 Irak | 0 | -4.05 |

### Grupo J

| Fecha | Partido | Pred. | P(1) | P(X) | P(2) |
|---|---|:-:|--:|--:|--:|
| 06-16 | 🇦🇷 Argentina – 🇩🇿 Argelia | **1-0** | 92% | 7% | 2% |
| 06-16 | 🇦🇹 Austria – 🇯🇴 Jordania | **1-0** | 98% | 2% | 0% |
| 06-22 | 🇦🇷 Argentina – 🇦🇹 Austria | **1-0** | 68% | 23% | 9% |
| 06-22 | 🇯🇴 Jordania – 🇩🇿 Argelia | **0-1** | 2% | 4% | 94% |
| 06-27 | 🇩🇿 Argelia – 🇦🇹 Austria | **0-1** | 13% | 28% | 60% |
| 06-27 | 🇯🇴 Jordania – 🇦🇷 Argentina | **0-2** | 0% | 0% | 100% |

| Pos | Equipo | Pts | DG (xG) |
|---|---|--:|--:|
| 1 | 🇦🇷 Argentina ✅ | 9 | +3.74 |
| 2 | 🇦🇹 Austria ✅ | 6 | +0.85 |
| 3 | 🇩🇿 Argelia 🟡 | 3 | -0.05 |
| 4 | 🇯🇴 Jordania | 0 | -4.54 |

### Grupo K

| Fecha | Partido | Pred. | P(1) | P(X) | P(2) |
|---|---|:-:|--:|--:|--:|
| 06-17 | 🇵🇹 Portugal – 🇨🇩 RD Congo | **1-0** | 97% | 2% | 1% |
| 06-17 | 🇺🇿 Uzbekistán – 🇨🇴 Colombia | **0-1** | 2% | 8% | 90% |
| 06-23 | 🇵🇹 Portugal – 🇺🇿 Uzbekistán | **2-0** | 95% | 5% | 1% |
| 06-23 | 🇨🇴 Colombia – 🇨🇩 RD Congo | **1-0** | 90% | 7% | 3% |
| 06-27 | 🇨🇩 RD Congo – 🇺🇿 Uzbekistán | **1-0** | 47% | 16% | 37% |
| 06-27 | 🇨🇴 Colombia – 🇵🇹 Portugal | **0-1** | 5% | 14% | 81% |

| Pos | Equipo | Pts | DG (xG) |
|---|---|--:|--:|
| 1 | 🇵🇹 Portugal ✅ | 9 | +2.93 |
| 2 | 🇨🇴 Colombia ✅ | 6 | +1.06 |
| 3 | 🇨🇩 RD Congo 🟡 | 3 | -1.43 |
| 4 | 🇺🇿 Uzbekistán | 0 | -2.56 |

### Grupo L

| Fecha | Partido | Pred. | P(1) | P(X) | P(2) |
|---|---|:-:|--:|--:|--:|
| 06-17 | 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra – 🇭🇷 Croacia | **2-1** | 75% | 19% | 5% |
| 06-17 | 🇬🇭 Ghana – 🇵🇦 Panamá | **0-1** | 4% | 15% | 81% |
| 06-23 | 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra – 🇬🇭 Ghana | **2-0** | 98% | 2% | 0% |
| 06-23 | 🇵🇦 Panamá – 🇭🇷 Croacia | **0-1** | 2% | 6% | 92% |
| 06-27 | 🇭🇷 Croacia – 🇬🇭 Ghana | **2-0** | 96% | 4% | 0% |
| 06-27 | 🇵🇦 Panamá – 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra | **0-2** | 0% | 2% | 97% |

| Pos | Equipo | Pts | DG (xG) |
|---|---|--:|--:|
| 1 | 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra ✅ | 9 | +3.56 |
| 2 | 🇭🇷 Croacia ✅ | 6 | +2.26 |
| 3 | 🇵🇦 Panamá 🟡 | 3 | -2.12 |
| 4 | 🇬🇭 Ghana | 0 | -3.70 |

✅ clasificado directo · 🟡 tercero (pasan los 8 mejores)

## Eliminatorias — 32 partidos

Si el empate es el resultado más probable, el cruce se decide por penaltis a favor del equipo con mayor probabilidad de victoria.

### Dieciseisavos de final (16 cruces) · *28 jun - 3 jul*

| Cruce | Pred. | Avanza | P(1) | P(X) | P(2) |
|---|:-:|---|--:|--:|--:|
| 🇩🇪 Alemania – 🇹🇷 Turquía | **2-1** | **🇩🇪 Alemania** | 68% | 23% | 9% |
| 🇫🇷 Francia – 🇮🇷 Irán | **1-0** | **🇫🇷 Francia** | 72% | 20% | 8% |
| 🇰🇷 Corea del Sur – 🇨🇦 Canadá | **1-1 (pen)** | **🇰🇷 Corea del Sur** | 37% | 39% | 24% |
| 🇳🇱 Países Bajos – 🇲🇦 Marruecos | **1-0** | **🇳🇱 Países Bajos** | 43% | 27% | 30% |
| 🇨🇴 Colombia – 🇭🇷 Croacia | **0-1** | **🇭🇷 Croacia** | 14% | 24% | 62% |
| 🇪🇸 España – 🇦🇹 Austria | **2-1** | **🇪🇸 España** | 53% | 33% | 14% |
| 🇺🇸 EE. UU. – 🇧🇦 Bosnia-Herzegovina | **1-0** | **🇺🇸 EE. UU.** | 54% | 25% | 21% |
| 🇧🇪 Bélgica – 🇨🇻 Cabo Verde | **2-0** | **🇧🇪 Bélgica** | 75% | 17% | 7% |
| 🇧🇷 Brasil – 🇯🇵 Japón | **1-0** | **🇧🇷 Brasil** | 47% | 35% | 18% |
| 🇨🇮 Costa de Marfil – 🇸🇳 Senegal | **0-1** | **🇸🇳 Senegal** | 18% | 30% | 51% |
| 🇲🇽 México – 🇸🇪 Suecia | **2-1** | **🇲🇽 México** | 69% | 22% | 9% |
| 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra – 🇩🇿 Argelia | **1-0** | **🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra** | 77% | 14% | 9% |
| 🇦🇷 Argentina – 🇺🇾 Uruguay | **1-0** | **🇦🇷 Argentina** | 64% | 25% | 12% |
| 🇦🇺 Australia – 🇪🇬 Egipto | **1-0** | **🇦🇺 Australia** | 46% | 22% | 31% |
| 🇨🇭 Suiza – 🏴󠁧󠁢󠁳󠁣󠁴󠁿 Escocia | **2-1** | **🇨🇭 Suiza** | 66% | 23% | 11% |
| 🇵🇹 Portugal – 🇪🇨 Ecuador | **1-0** | **🇵🇹 Portugal** | 70% | 19% | 11% |

### Octavos de final · *4 - 7 jul*

| Cruce | Pred. | Avanza | P(1) | P(X) | P(2) |
|---|:-:|---|--:|--:|--:|
| 🇩🇪 Alemania – 🇫🇷 Francia | **1-2** | **🇫🇷 Francia** | 19% | 34% | 48% |
| 🇰🇷 Corea del Sur – 🇳🇱 Países Bajos | **0-1** | **🇳🇱 Países Bajos** | 11% | 32% | 57% |
| 🇭🇷 Croacia – 🇪🇸 España | **1-2** | **🇪🇸 España** | 11% | 39% | 49% |
| 🇺🇸 EE. UU. – 🇧🇪 Bélgica | **0-1** | **🇧🇪 Bélgica** | 6% | 23% | 71% |
| 🇧🇷 Brasil – 🇸🇳 Senegal | **0-1** | **🇸🇳 Senegal** | 35% | 30% | 35% |
| 🇲🇽 México – 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra | **0-1** | **🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra** | 9% | 18% | 73% |
| 🇦🇷 Argentina – 🇦🇺 Australia | **2-0** | **🇦🇷 Argentina** | 80% | 14% | 6% |
| 🇨🇭 Suiza – 🇵🇹 Portugal | **1-2** | **🇵🇹 Portugal** | 16% | 25% | 59% |

### Cuartos de final · *9 - 11 jul*

| Cruce | Pred. | Avanza | P(1) | P(X) | P(2) |
|---|:-:|---|--:|--:|--:|
| 🇫🇷 Francia – 🇳🇱 Países Bajos | **2-1** | **🇫🇷 Francia** | 53% | 30% | 17% |
| 🇪🇸 España – 🇧🇪 Bélgica | **2-1** | **🇪🇸 España** | 46% | 44% | 10% |
| 🇸🇳 Senegal – 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra | **0-1** | **🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra** | 17% | 27% | 56% |
| 🇦🇷 Argentina – 🇵🇹 Portugal | **2-1** | **🇦🇷 Argentina** | 43% | 39% | 18% |

### Semifinales · *14 - 15 jul*

| Cruce | Pred. | Avanza | P(1) | P(X) | P(2) |
|---|:-:|---|--:|--:|--:|
| 🇫🇷 Francia – 🇪🇸 España | **1-1 (pen)** | **🇫🇷 Francia** | 32% | 40% | 28% |
| 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra – 🇦🇷 Argentina | **0-1** | **🇦🇷 Argentina** | 30% | 35% | 35% |

### Partido por el 3er puesto · *18 jul*

| Cruce | Pred. | Avanza | P(1) | P(X) | P(2) |
|---|:-:|---|--:|--:|--:|
| 🇪🇸 España – 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra | **1-1 (pen)** | **🇪🇸 España** | 35% | 40% | 25% |

### 🏆 Gran Final — MetLife Stadium, Nueva York/Nueva Jersey · *19 jul*

| Cruce | Pred. | Avanza | P(1) | P(X) | P(2) |
|---|:-:|---|--:|--:|--:|
| 🇫🇷 Francia – 🇦🇷 Argentina | **1-0** | **🇫🇷 Francia** | 42% | 32% | 26% |

## Probabilidades por selección — 10.000 mundiales simulados

| Selección | Pasa grupos | Octavos | Cuartos | Semis | Final | 🏆 Campeón |
|---|--:|--:|--:|--:|--:|--:|
| 🇫🇷 Francia | 100.0% | 93.7% | 70.0% | 59.8% | 38.8% | **27.9%** |
| 🇪🇸 España | 99.9% | 78.2% | 64.2% | 54.7% | 32.5% | **20.2%** |
| 🇦🇷 Argentina | 100.0% | 81.5% | 73.2% | 55.1% | 35.1% | **17.6%** |
| 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra | 100.0% | 92.8% | 81.0% | 63.5% | 38.2% | **17.4%** |
| 🇩🇪 Alemania | 100.0% | 88.5% | 29.9% | 17.8% | 8.5% | **4.1%** |
| 🇵🇹 Portugal | 100.0% | 85.9% | 69.5% | 32.0% | 13.1% | **3.9%** |
| 🇧🇪 Bélgica | 99.8% | 90.2% | 78.9% | 25.4% | 8.1% | **3.0%** |
| 🇳🇱 Países Bajos | 99.8% | 57.8% | 46.6% | 16.2% | 6.4% | **2.2%** |
| 🇭🇷 Croacia | 99.8% | 80.2% | 23.8% | 11.9% | 3.5% | **0.9%** |
| 🇧🇷 Brasil | 100.0% | 68.0% | 40.1% | 12.6% | 4.6% | **0.9%** |
| 🇸🇳 Senegal | 98.3% | 66.3% | 34.4% | 11.0% | 3.0% | **0.5%** |
| 🇲🇦 Marruecos | 99.9% | 46.8% | 32.7% | 6.9% | 1.9% | **0.4%** |
| 🇦🇹 Austria | 99.4% | 26.5% | 11.4% | 3.9% | 0.9% | **0.2%** |
| 🇲🇽 México | 100.0% | 79.7% | 14.8% | 5.1% | 1.3% | **0.2%** |
| 🇺🇾 Uruguay | 86.4% | 16.8% | 11.1% | 3.7% | 0.7% | **0.2%** |
| 🇯🇵 Japón | 99.9% | 29.2% | 13.7% | 2.8% | 0.7% | **0.1%** |
| 🇮🇷 Irán | 77.3% | 29.7% | 7.3% | 2.0% | 0.4% | **0.1%** |
| 🇨🇭 Suiza | 88.1% | 53.9% | 15.3% | 3.1% | 0.4% | **0.1%** |
| 🇹🇷 Turquía | 79.8% | 30.9% | 8.2% | 2.0% | 0.4% | **0.0%** |
| 🇨🇮 Costa de Marfil | 100.0% | 33.2% | 9.8% | 1.8% | 0.3% | **0.0%** |
| 🇨🇴 Colombia | 99.1% | 22.1% | 5.9% | 1.8% | 0.3% | **0.0%** |
| 🇦🇺 Australia | 99.8% | 51.1% | 7.2% | 1.1% | 0.2% | **0.0%** |
| 🇺🇸 EE. UU. | 99.9% | 50.9% | 6.7% | 0.7% | 0.1% | **0.0%** |
| 🇳🇴 Noruega | 76.6% | 23.0% | 6.3% | 1.3% | 0.2% | **0.0%** |
| 🇪🇨 Ecuador | 76.2% | 16.2% | 4.3% | 0.7% | 0.0% | **0.0%** |
| 🇨🇦 Canadá | 87.7% | 41.5% | 7.5% | 0.9% | 0.1% | **0.0%** |
| 🇰🇷 Corea del Sur | 100.0% | 64.2% | 12.6% | 0.8% | 0.1% | **0.0%** |
| 🇩🇿 Argelia | 93.7% | 17.5% | 4.0% | 0.6% | 0.0% | **0.0%** |
| 🇪🇬 Egipto | 93.5% | 31.1% | 3.3% | 0.4% | 0.0% | **0.0%** |
| 🇨🇻 Cabo Verde | 68.6% | 8.9% | 1.2% | 0.1% | 0.0% | **0.0%** |
| 🇿🇦 Sudáfrica | 17.8% | 3.0% | 0.5% | 0.1% | 0.0% | **0.0%** |
| 🇨🇿 República Checa | 11.8% | 1.8% | 0.4% | 0.0% | 0.0% | **0.0%** |
| 🇸🇪 Suecia | 99.5% | 12.3% | 1.7% | 0.1% | 0.0% | **0.0%** |
| 🏴󠁧󠁢󠁳󠁣󠁴󠁿 Escocia | 94.3% | 10.2% | 1.1% | 0.1% | 0.0% | **0.0%** |
| 🇵🇦 Panamá | 16.2% | 1.9% | 0.3% | 0.0% | 0.0% | **0.0%** |
| 🇨🇩 RD Congo | 17.5% | 1.8% | 0.3% | 0.0% | 0.0% | **0.0%** |
| 🇧🇦 Bosnia-Herzegovina | 48.7% | 7.0% | 0.7% | 0.0% | 0.0% | **0.0%** |
| 🇶🇦 Catar | 42.7% | 3.7% | 0.2% | 0.0% | 0.0% | **0.0%** |
| 🇺🇿 Uzbekistán | 7.3% | 0.7% | 0.1% | 0.0% | 0.0% | **0.0%** |
| 🇸🇦 Arabia Saudí | 16.4% | 0.6% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🇨🇼 Curazao | 0.1% | 0.0% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🇬🇭 Ghana | 0.5% | 0.1% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🇭🇹 Haití | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🇮🇶 Irak | 0.2% | 0.0% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🇯🇴 Jordania | 0.2% | 0.0% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🇳🇿 Nueva Zelanda | 1.2% | 0.1% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🇵🇾 Paraguay | 2.2% | 0.4% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🇹🇳 Túnez | 0.1% | 0.0% | 0.0% | 0.0% | 0.0% | **0.0%** |

## Validación con los partidos ya jugados

| Partido | Predicción (1X2 máx) | Resultado real | ¿Acierto? |
|---|:-:|:-:|:-:|
| 🇲🇽 México – 🇿🇦 Sudáfrica | México (85%) | 2-0 | ✅ |
| 🇰🇷 Corea del Sur – 🇨🇿 República Checa | Corea del Sur (68%) | 2-1 | ✅ |
| 🇨🇦 Canadá – 🇧🇦 Bosnia-Herzegovina | Canadá (77%) | 1-1 | ❌ |
| 🇶🇦 Catar – 🇨🇭 Suiza | Suiza (91%) | 1-1 | ❌ |
| 🇧🇷 Brasil – 🇲🇦 Marruecos | Marruecos (42%) | 1-1 | ❌ |
| 🇭🇹 Haití – 🏴󠁧󠁢󠁳󠁣󠁴󠁿 Escocia | Escocia (89%) | 0-1 | ✅ |
| 🇺🇸 EE. UU. – 🇵🇾 Paraguay | EE. UU. (63%) | 4-1 | ✅ |
| 🇦🇺 Australia – 🇹🇷 Turquía | Turquía (54%) | 2-0 | ❌ |
| 🇩🇪 Alemania – 🇨🇼 Curazao | Alemania (99%) | 7-1 | ✅ |
| 🇨🇮 Costa de Marfil – 🇪🇨 Ecuador | Costa de Marfil (58%) | 1-0 | ✅ |
| 🇳🇱 Países Bajos – 🇯🇵 Japón | Países Bajos (63%) | 2-2 | ❌ |
| 🇸🇪 Suecia – 🇹🇳 Túnez | Suecia (46%) | 5-1 | ✅ |
| 🇧🇪 Bélgica – 🇪🇬 Egipto | Bélgica (94%) | 1-1 | ❌ |
| 🇮🇷 Irán – 🇳🇿 Nueva Zelanda | Irán (91%) | 2-2 | ❌ |
| 🇪🇸 España – 🇨🇻 Cabo Verde | España (92%) | 0-0 | ❌ |
| 🇸🇦 Arabia Saudí – 🇺🇾 Uruguay | Uruguay (96%) | 1-1 | ❌ |

**Aciertos de ganador: 7/16 (44%).** Las probabilidades de campeón y de clasificación de arriba ya están *condicionadas* a estos resultados: los partidos jugados se fijan y solo se simulan los que faltan.

---
*Predicciones generadas automáticamente con `prediccion_mundial.py`. El fútbol, por suerte, no entiende de modelos.* ⚽
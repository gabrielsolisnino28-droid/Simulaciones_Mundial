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
| 1 | 🇫🇷 Francia | **27.2%** | 38.5% | 58.8% | 69.7% |
| 2 | 🇦🇷 Argentina | **23.6%** | 47.7% | 74.3% | 86.9% |
| 3 | 🇪🇸 España | **18.9%** | 31.4% | 52.8% | 62.5% |
| 4 | 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra | **16.3%** | 36.9% | 65.8% | 80.3% |
| 5 | 🇩🇪 Alemania | **3.9%** | 7.7% | 17.2% | 29.8% |
| 6 | 🇧🇪 Bélgica | **3.4%** | 8.7% | 28.3% | 89.0% |
| 7 | 🇳🇱 Países Bajos | **2.2%** | 6.6% | 17.0% | 52.0% |
| 8 | 🇵🇹 Portugal | **1.2%** | 3.6% | 10.6% | 18.6% |
| 9 | 🇧🇷 Brasil | **1.0%** | 5.4% | 16.8% | 51.6% |
| 10 | 🇸🇳 Senegal | **0.6%** | 3.8% | 11.0% | 43.0% |

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
| 1 | 🇲🇽 México ✅ | 9 | +6.00 |
| 2 | 🇿🇦 Sudáfrica ✅ | 4 | -1.00 |
| 3 | 🇰🇷 Corea del Sur 🟡 | 3 | -1.00 |
| 4 | 🇨🇿 República Checa | 1 | -4.00 |

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
| 1 | 🇨🇭 Suiza ✅ | 7 | +4.00 |
| 2 | 🇨🇦 Canadá ✅ | 4 | +5.00 |
| 3 | 🇧🇦 Bosnia-Herzegovina 🟡 | 4 | -1.00 |
| 4 | 🇶🇦 Catar | 1 | -8.00 |

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
| 1 | 🇧🇷 Brasil ✅ | 7 | +6.00 |
| 2 | 🇲🇦 Marruecos ✅ | 7 | +3.00 |
| 3 | 🏴󠁧󠁢󠁳󠁣󠁴󠁿 Escocia 🟡 | 3 | -3.00 |
| 4 | 🇭🇹 Haití | 0 | -6.00 |

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
| 1 | 🇺🇸 EE. UU. ✅ | 6 | +4.00 |
| 2 | 🇦🇺 Australia ✅ | 4 | +0.00 |
| 3 | 🇵🇾 Paraguay 🟡 | 4 | -2.00 |
| 4 | 🇹🇷 Turquía | 3 | -2.00 |

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
| 1 | 🇩🇪 Alemania ✅ | 6 | +6.00 |
| 2 | 🇨🇮 Costa de Marfil ✅ | 6 | +2.00 |
| 3 | 🇪🇨 Ecuador 🟡 | 4 | +0.00 |
| 4 | 🇨🇼 Curazao | 1 | -8.00 |

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
| 1 | 🇳🇱 Países Bajos ✅ | 7 | +6.00 |
| 2 | 🇯🇵 Japón ✅ | 5 | +4.00 |
| 3 | 🇸🇪 Suecia 🟡 | 4 | +0.00 |
| 4 | 🇹🇳 Túnez | 0 | -10.00 |

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
| 1 | 🇧🇪 Bélgica ✅ | 5 | +4.00 |
| 2 | 🇪🇬 Egipto ✅ | 5 | +2.00 |
| 3 | 🇮🇷 Irán 🟡 | 3 | +0.00 |
| 4 | 🇳🇿 Nueva Zelanda | 1 | -6.00 |

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
| 1 | 🇪🇸 España ✅ | 7 | +5.00 |
| 2 | 🇨🇻 Cabo Verde ✅ | 3 | +0.00 |
| 3 | 🇺🇾 Uruguay 🟡 | 2 | -1.00 |
| 4 | 🇸🇦 Arabia Saudí | 2 | -4.00 |

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
| 1 | 🇫🇷 Francia ✅ | 9 | +8.00 |
| 2 | 🇳🇴 Noruega ✅ | 6 | +1.00 |
| 3 | 🇸🇳 Senegal 🟡 | 3 | +2.00 |
| 4 | 🇮🇶 Irak | 0 | -11.00 |

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
| 1 | 🇦🇷 Argentina ✅ | 9 | +7.00 |
| 2 | 🇦🇹 Austria ✅ | 4 | +0.00 |
| 3 | 🇩🇿 Argelia 🟡 | 4 | -2.00 |
| 4 | 🇯🇴 Jordania | 0 | -5.00 |

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
| 1 | 🇨🇴 Colombia ✅ | 7 | +3.00 |
| 2 | 🇵🇹 Portugal ✅ | 5 | +5.00 |
| 3 | 🇨🇩 RD Congo 🟡 | 4 | +1.00 |
| 4 | 🇺🇿 Uzbekistán | 0 | -9.00 |

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
| 1 | 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra ✅ | 7 | +4.00 |
| 2 | 🇭🇷 Croacia ✅ | 6 | +0.00 |
| 3 | 🇬🇭 Ghana 🟡 | 4 | +0.00 |
| 4 | 🇵🇦 Panamá | 0 | -4.00 |

✅ clasificado directo · 🟡 tercero (pasan los 8 mejores)

## Eliminatorias — 32 partidos

Si el empate es el resultado más probable, el cruce se decide por penaltis a favor del equipo con mayor probabilidad de victoria.

### Dieciseisavos de final (16 cruces) · *28 jun - 3 jul*

| Cruce | Pred. | Avanza | P(1) | P(X) | P(2) |
|---|:-:|---|--:|--:|--:|
| 🇩🇪 Alemania – 🇨🇩 RD Congo | **1-0** | **🇩🇪 Alemania** | 87% | 11% | 2% |
| 🇫🇷 Francia – 🇸🇪 Suecia | **2-0** | **🇫🇷 Francia** | 85% | 11% | 4% |
| 🇿🇦 Sudáfrica – 🇨🇦 Canadá | **0-1** | **🇨🇦 Canadá** | 12% | 36% | 52% |
| 🇳🇱 Países Bajos – 🇲🇦 Marruecos | **1-0** | **🇳🇱 Países Bajos** | 43% | 27% | 30% |
| 🇵🇹 Portugal – 🇭🇷 Croacia | **2-1** | **🇵🇹 Portugal** | 42% | 29% | 29% |
| 🇪🇸 España – 🇦🇹 Austria | **2-1** | **🇪🇸 España** | 53% | 33% | 14% |
| 🇺🇸 EE. UU. – 🇪🇨 Ecuador | **1-0** | **🇺🇸 EE. UU.** | 39% | 29% | 31% |
| 🇧🇪 Bélgica – 🇬🇭 Ghana | **2-0** | **🇧🇪 Bélgica** | 87% | 11% | 2% |
| 🇧🇷 Brasil – 🇯🇵 Japón | **1-0** | **🇧🇷 Brasil** | 47% | 35% | 18% |
| 🇨🇮 Costa de Marfil – 🇳🇴 Noruega | **1-0** | **🇨🇮 Costa de Marfil** | 48% | 25% | 28% |
| 🇲🇽 México – 🇧🇦 Bosnia-Herzegovina | **1-0** | **🇲🇽 México** | 66% | 22% | 12% |
| 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra – 🇩🇿 Argelia | **1-0** | **🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra** | 77% | 14% | 9% |
| 🇦🇷 Argentina – 🇨🇻 Cabo Verde | **2-0** | **🇦🇷 Argentina** | 76% | 18% | 6% |
| 🇦🇺 Australia – 🇪🇬 Egipto | **1-0** | **🇦🇺 Australia** | 46% | 22% | 31% |
| 🇨🇭 Suiza – 🇵🇾 Paraguay | **1-0** | **🇨🇭 Suiza** | 70% | 17% | 13% |
| 🇨🇴 Colombia – 🇸🇳 Senegal | **0-1** | **🇸🇳 Senegal** | 30% | 27% | 43% |

### Octavos de final · *4 - 7 jul*

| Cruce | Pred. | Avanza | P(1) | P(X) | P(2) |
|---|:-:|---|--:|--:|--:|
| 🇩🇪 Alemania – 🇫🇷 Francia | **1-2** | **🇫🇷 Francia** | 19% | 34% | 48% |
| 🇨🇦 Canadá – 🇳🇱 Países Bajos | **0-1** | **🇳🇱 Países Bajos** | 9% | 30% | 60% |
| 🇵🇹 Portugal – 🇪🇸 España | **1-2** | **🇪🇸 España** | 14% | 40% | 46% |
| 🇺🇸 EE. UU. – 🇧🇪 Bélgica | **0-1** | **🇧🇪 Bélgica** | 6% | 23% | 71% |
| 🇧🇷 Brasil – 🇨🇮 Costa de Marfil | **1-0** | **🇧🇷 Brasil** | 47% | 33% | 20% |
| 🇲🇽 México – 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra | **0-1** | **🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra** | 9% | 18% | 73% |
| 🇦🇷 Argentina – 🇦🇺 Australia | **2-0** | **🇦🇷 Argentina** | 80% | 14% | 6% |
| 🇨🇭 Suiza – 🇸🇳 Senegal | **0-1** | **🇸🇳 Senegal** | 22% | 29% | 49% |

### Cuartos de final · *9 - 11 jul*

| Cruce | Pred. | Avanza | P(1) | P(X) | P(2) |
|---|:-:|---|--:|--:|--:|
| 🇫🇷 Francia – 🇳🇱 Países Bajos | **2-1** | **🇫🇷 Francia** | 53% | 30% | 17% |
| 🇪🇸 España – 🇧🇪 Bélgica | **2-1** | **🇪🇸 España** | 46% | 44% | 10% |
| 🇧🇷 Brasil – 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra | **0-1** | **🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra** | 16% | 29% | 55% |
| 🇦🇷 Argentina – 🇸🇳 Senegal | **1-0** | **🇦🇷 Argentina** | 62% | 26% | 12% |

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
| 🇫🇷 Francia | 100.0% | 96.0% | 69.7% | 58.8% | 38.5% | **27.2%** |
| 🇦🇷 Argentina | 100.0% | 92.9% | 86.9% | 74.3% | 47.7% | **23.6%** |
| 🇪🇸 España | 100.0% | 79.0% | 62.5% | 52.8% | 31.4% | **18.9%** |
| 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra | 100.0% | 89.5% | 80.3% | 65.8% | 36.9% | **16.3%** |
| 🇩🇪 Alemania | 100.0% | 97.3% | 29.8% | 17.2% | 7.7% | **3.9%** |
| 🇧🇪 Bélgica | 100.0% | 97.4% | 89.0% | 28.3% | 8.7% | **3.4%** |
| 🇳🇱 Países Bajos | 100.0% | 58.9% | 52.0% | 17.0% | 6.6% | **2.2%** |
| 🇵🇹 Portugal | 100.0% | 59.4% | 18.6% | 10.6% | 3.6% | **1.2%** |
| 🇧🇷 Brasil | 100.0% | 71.1% | 51.6% | 16.8% | 5.4% | **1.0%** |
| 🇸🇳 Senegal | 100.0% | 58.3% | 43.0% | 11.0% | 3.8% | **0.6%** |
| 🇭🇷 Croacia | 100.0% | 40.6% | 11.5% | 5.2% | 1.4% | **0.4%** |
| 🇲🇦 Marruecos | 100.0% | 41.1% | 31.9% | 6.0% | 1.5% | **0.3%** |
| 🇲🇽 México | 100.0% | 85.4% | 15.4% | 7.3% | 1.8% | **0.2%** |
| 🇯🇵 Japón | 100.0% | 28.9% | 19.2% | 4.2% | 1.0% | **0.2%** |
| 🇨🇴 Colombia | 100.0% | 41.7% | 29.2% | 7.4% | 1.3% | **0.1%** |
| 🇨🇭 Suiza | 100.0% | 84.3% | 26.4% | 4.6% | 0.7% | **0.1%** |
| 🇦🇹 Austria | 100.0% | 21.0% | 7.4% | 2.2% | 0.4% | **0.1%** |
| 🇨🇮 Costa de Marfil | 100.0% | 63.1% | 19.7% | 3.6% | 0.6% | **0.1%** |
| 🇳🇴 Noruega | 100.0% | 36.9% | 9.5% | 1.7% | 0.4% | **0.0%** |
| 🇦🇺 Australia | 100.0% | 58.7% | 7.0% | 1.7% | 0.2% | **0.0%** |
| 🇺🇸 EE. UU. | 100.0% | 54.9% | 5.5% | 0.4% | 0.0% | **0.0%** |
| 🇩🇿 Argelia | 100.0% | 10.5% | 3.3% | 0.6% | 0.1% | **0.0%** |
| 🇨🇦 Canadá | 100.0% | 80.7% | 14.1% | 0.8% | 0.1% | **0.0%** |
| 🇨🇻 Cabo Verde | 100.0% | 7.1% | 1.9% | 0.4% | 0.0% | **0.0%** |
| 🇪🇬 Egipto | 100.0% | 41.3% | 4.2% | 0.6% | 0.1% | **0.0%** |
| 🇪🇨 Ecuador | 100.0% | 45.1% | 5.0% | 0.4% | 0.1% | **0.0%** |
| 🇵🇾 Paraguay | 100.0% | 15.7% | 1.4% | 0.2% | 0.0% | **0.0%** |
| 🇿🇦 Sudáfrica | 100.0% | 19.3% | 2.1% | 0.1% | 0.0% | **0.0%** |
| 🇧🇦 Bosnia-Herzegovina | 100.0% | 14.6% | 0.9% | 0.1% | 0.0% | **0.0%** |
| 🇸🇪 Suecia | 100.0% | 4.0% | 0.3% | 0.0% | 0.0% | **0.0%** |
| 🇬🇭 Ghana | 100.0% | 2.6% | 0.4% | 0.0% | 0.0% | **0.0%** |
| 🇨🇩 RD Congo | 100.0% | 2.7% | 0.2% | 0.0% | 0.0% | **0.0%** |
| 🇸🇦 Arabia Saudí | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🇶🇦 Catar | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🇰🇷 Corea del Sur | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🇨🇼 Curazao | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🏴󠁧󠁢󠁳󠁣󠁴󠁿 Escocia | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🇭🇹 Haití | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🇮🇶 Irak | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🇮🇷 Irán | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🇯🇴 Jordania | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🇳🇿 Nueva Zelanda | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🇵🇦 Panamá | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🇨🇿 República Checa | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🇹🇷 Turquía | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🇹🇳 Túnez | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🇺🇾 Uruguay | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🇺🇿 Uzbekistán | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | **0.0%** |

## Validación con los partidos ya jugados

| Partido | Predicción (1X2 máx) | Resultado real | ¿Acierto? |
|---|:-:|:-:|:-:|
| 🇲🇽 México – 🇿🇦 Sudáfrica | México (85%) | 2-0 | ✅ |
| 🇰🇷 Corea del Sur – 🇨🇿 República Checa | Corea del Sur (68%) | 2-1 | ✅ |
| 🇨🇿 República Checa – 🇿🇦 Sudáfrica | Sudáfrica (41%) | 1-1 | ❌ |
| 🇲🇽 México – 🇰🇷 Corea del Sur | México (60%) | 1-0 | ✅ |
| 🇿🇦 Sudáfrica – 🇰🇷 Corea del Sur | Corea del Sur (64%) | 1-0 | ❌ |
| 🇨🇿 República Checa – 🇲🇽 México | México (88%) | 0-3 | ✅ |
| 🇨🇦 Canadá – 🇧🇦 Bosnia-Herzegovina | Canadá (77%) | 1-1 | ❌ |
| 🇶🇦 Catar – 🇨🇭 Suiza | Suiza (91%) | 1-1 | ❌ |
| 🇨🇭 Suiza – 🇧🇦 Bosnia-Herzegovina | Suiza (74%) | 4-1 | ✅ |
| 🇨🇦 Canadá – 🇶🇦 Catar | Canadá (68%) | 6-0 | ✅ |
| 🇧🇦 Bosnia-Herzegovina – 🇶🇦 Catar | Bosnia-Herzegovina (39%) | 3-1 | ✅ |
| 🇨🇭 Suiza – 🇨🇦 Canadá | Suiza (35%) | 2-1 | ✅ |
| 🇧🇷 Brasil – 🇲🇦 Marruecos | Marruecos (42%) | 1-1 | ❌ |
| 🇭🇹 Haití – 🏴󠁧󠁢󠁳󠁣󠁴󠁿 Escocia | Escocia (89%) | 0-1 | ✅ |
| 🏴󠁧󠁢󠁳󠁣󠁴󠁿 Escocia – 🇲🇦 Marruecos | Marruecos (87%) | 0-1 | ✅ |
| 🇧🇷 Brasil – 🇭🇹 Haití | Brasil (99%) | 3-0 | ✅ |
| 🇲🇦 Marruecos – 🇭🇹 Haití | Marruecos (97%) | 4-2 | ✅ |
| 🏴󠁧󠁢󠁳󠁣󠁴󠁿 Escocia – 🇧🇷 Brasil | Brasil (92%) | 0-3 | ✅ |
| 🇺🇸 EE. UU. – 🇵🇾 Paraguay | EE. UU. (63%) | 4-1 | ✅ |
| 🇦🇺 Australia – 🇹🇷 Turquía | Turquía (54%) | 2-0 | ❌ |
| 🇺🇸 EE. UU. – 🇦🇺 Australia | EE. UU. (54%) | 2-0 | ✅ |
| 🇹🇷 Turquía – 🇵🇾 Paraguay | Turquía (84%) | 0-1 | ❌ |
| 🇵🇾 Paraguay – 🇦🇺 Australia | Australia (76%) | 0-0 | ❌ |
| 🇹🇷 Turquía – 🇺🇸 EE. UU. | Turquía (48%) | 3-2 | ✅ |
| 🇩🇪 Alemania – 🇨🇼 Curazao | Alemania (99%) | 7-1 | ✅ |
| 🇨🇮 Costa de Marfil – 🇪🇨 Ecuador | Costa de Marfil (58%) | 1-0 | ✅ |
| 🇩🇪 Alemania – 🇨🇮 Costa de Marfil | Alemania (89%) | 2-1 | ✅ |
| 🇪🇨 Ecuador – 🇨🇼 Curazao | Ecuador (95%) | 0-0 | ❌ |
| 🇨🇼 Curazao – 🇨🇮 Costa de Marfil | Costa de Marfil (95%) | 0-2 | ✅ |
| 🇪🇨 Ecuador – 🇩🇪 Alemania | Alemania (91%) | 2-1 | ❌ |
| 🇳🇱 Países Bajos – 🇯🇵 Japón | Países Bajos (63%) | 2-2 | ❌ |
| 🇸🇪 Suecia – 🇹🇳 Túnez | Suecia (46%) | 5-1 | ✅ |
| 🇳🇱 Países Bajos – 🇸🇪 Suecia | Países Bajos (90%) | 5-1 | ✅ |
| 🇹🇳 Túnez – 🇯🇵 Japón | Japón (95%) | 0-4 | ✅ |
| 🇯🇵 Japón – 🇸🇪 Suecia | Japón (92%) | 1-1 | ❌ |
| 🇹🇳 Túnez – 🇳🇱 Países Bajos | Países Bajos (95%) | 1-3 | ✅ |
| 🇧🇪 Bélgica – 🇪🇬 Egipto | Bélgica (94%) | 1-1 | ❌ |
| 🇮🇷 Irán – 🇳🇿 Nueva Zelanda | Irán (91%) | 2-2 | ❌ |
| 🇧🇪 Bélgica – 🇮🇷 Irán | Bélgica (76%) | 0-0 | ❌ |
| 🇳🇿 Nueva Zelanda – 🇪🇬 Egipto | Egipto (91%) | 1-3 | ✅ |
| 🇳🇿 Nueva Zelanda – 🇧🇪 Bélgica | Bélgica (98%) | 1-5 | ✅ |
| 🇪🇬 Egipto – 🇮🇷 Irán | Irán (72%) | 1-1 | ❌ |
| 🇪🇸 España – 🇨🇻 Cabo Verde | España (92%) | 0-0 | ❌ |
| 🇸🇦 Arabia Saudí – 🇺🇾 Uruguay | Uruguay (96%) | 1-1 | ❌ |
| 🇪🇸 España – 🇸🇦 Arabia Saudí | España (98%) | 4-0 | ✅ |
| 🇺🇾 Uruguay – 🇨🇻 Cabo Verde | Uruguay (85%) | 2-2 | ❌ |
| 🇺🇾 Uruguay – 🇪🇸 España | España (84%) | 0-1 | ✅ |
| 🇨🇻 Cabo Verde – 🇸🇦 Arabia Saudí | Cabo Verde (64%) | 0-0 | ❌ |
| 🇫🇷 Francia – 🇸🇳 Senegal | Francia (85%) | 3-1 | ✅ |
| 🇮🇶 Irak – 🇳🇴 Noruega | Noruega (95%) | 1-4 | ✅ |
| 🇫🇷 Francia – 🇮🇶 Irak | Francia (99%) | 3-0 | ✅ |
| 🇳🇴 Noruega – 🇸🇳 Senegal | Senegal (57%) | 3-2 | ❌ |
| 🇳🇴 Noruega – 🇫🇷 Francia | Francia (94%) | 1-4 | ✅ |
| 🇸🇳 Senegal – 🇮🇶 Irak | Senegal (96%) | 5-0 | ✅ |
| 🇦🇷 Argentina – 🇩🇿 Argelia | Argentina (92%) | 3-0 | ✅ |
| 🇦🇹 Austria – 🇯🇴 Jordania | Austria (98%) | 3-1 | ✅ |
| 🇦🇷 Argentina – 🇦🇹 Austria | Argentina (68%) | 2-0 | ✅ |
| 🇯🇴 Jordania – 🇩🇿 Argelia | Argelia (94%) | 1-2 | ✅ |
| 🇩🇿 Argelia – 🇦🇹 Austria | Austria (60%) | 3-3 | ❌ |
| 🇯🇴 Jordania – 🇦🇷 Argentina | Argentina (100%) | 1-3 | ✅ |
| 🇵🇹 Portugal – 🇨🇩 RD Congo | Portugal (97%) | 1-1 | ❌ |
| 🇺🇿 Uzbekistán – 🇨🇴 Colombia | Colombia (90%) | 1-3 | ✅ |
| 🇵🇹 Portugal – 🇺🇿 Uzbekistán | Portugal (95%) | 5-0 | ✅ |
| 🇨🇴 Colombia – 🇨🇩 RD Congo | Colombia (90%) | 1-0 | ✅ |
| 🇨🇩 RD Congo – 🇺🇿 Uzbekistán | RD Congo (47%) | 3-1 | ✅ |
| 🇨🇴 Colombia – 🇵🇹 Portugal | Portugal (81%) | 0-0 | ❌ |
| 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra – 🇭🇷 Croacia | Inglaterra (75%) | 4-2 | ✅ |
| 🇬🇭 Ghana – 🇵🇦 Panamá | Panamá (81%) | 1-0 | ❌ |
| 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra – 🇬🇭 Ghana | Inglaterra (98%) | 0-0 | ❌ |
| 🇵🇦 Panamá – 🇭🇷 Croacia | Croacia (92%) | 0-1 | ✅ |
| 🇭🇷 Croacia – 🇬🇭 Ghana | Croacia (96%) | 2-1 | ✅ |
| 🇵🇦 Panamá – 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra | Inglaterra (97%) | 0-2 | ✅ |

**Aciertos de ganador: 46/72 (64%).** Las probabilidades de campeón y de clasificación de arriba ya están *condicionadas* a estos resultados: los partidos jugados se fijan y solo se simulan los que faltan.

---
*Predicciones generadas automáticamente con `prediccion_mundial.py`. El fútbol, por suerte, no entiende de modelos.* ⚽
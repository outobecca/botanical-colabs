# 🔧 FMI API Troubleshooting Guide

## Common Issue: "No data received from FMI API"

If you're seeing this warning, don't worry! Here's how to fix it.

## Quick Fixes

### ✅ Solution 1: Use Sample Data (Easiest)
Select option **[11] Use sample data** in Step 2 configuration.
- Works offline
- No API issues
- Perfect for testing and demonstrations

### ✅ Solution 2: Run API Diagnostics
Before Step 4, run the **API Diagnostics** cell to identify the issue:
- Tests internet connectivity
- Checks FMI service status
- Validates station data availability
- Provides specific error messages

### ✅ Solution 3: Try Recent Dates
FMI API works best with recent data (last 30 days to 1 year):
- ✅ Good: Last 30 days, Current year, Growing season 2024
- ⚠️ May fail: Very old historical data
- Select option **[1] Last 30 days** for most reliable results

### ✅ Solution 4: Try Different Station
Some stations have more complete data than others:
- ✅ Best: Helsinki (#1), Jokioinen (#2), Tampere (#4)
- ⚠️ May have gaps: Smaller stations

## Why Does This Happen?

### 1. **FMI API Service Issues**
- The FMI API occasionally has downtime
- Check status: https://www.ilmatieteenlaitos.fi/avoin-data
- Usually temporary - try again later

### 2. **Data Availability**
- Not all stations have complete historical records
- Daily summary data may not be available for all parameters
- Some stations were installed recently

### 3. **Date Range Issues**
- Very old dates may not be available in daily summaries
- Future dates obviously won't have data
- Some stations don't have continuous records

### 4. **Network/Firewall Issues**
- Corporate/school firewalls may block the API
- VPNs might interfere
- Slow internet connections may timeout

## Detailed Solutions

### 🔍 Step 1: Run Diagnostics

Run the **API Diagnostics** cell (optional cell before Step 4) to see:

```
🔍 FMI API DIAGNOSTICS
======================================================================

1️⃣ Testing internet connectivity...
   ✅ FMI website reachable

2️⃣ Testing FMI WFS service...
   ✅ FMI WFS service responding

3️⃣ Testing stored queries...
   ✅ fmi::observations::weather::daily::simple
   ✅ fmi::observations::weather::daily::timevaluepair
   ✅ fmi::observations::weather::multipointcoverage

4️⃣ Testing data fetch for station...
   ✅ Data request successful
   ✅ Found 50 observation elements in response
```

If you see ❌ errors, that tells you exactly what's wrong.

### 🔧 Step 2: Adjust Settings

Based on diagnostic results:

#### If "Internet connectivity" fails:
- Check your internet connection
- Try disabling VPN
- Use sample data option

#### If "WFS service" fails:
- FMI API is down - try later
- Check https://www.ilmatieteenlaitos.fi/
- Use sample data option

#### If "No observations found":
- Station doesn't have data for that period
- Try selecting a different station
- Try a more recent date range
- Select "Last 30 days" instead of custom dates

### 📅 Step 3: Choose Better Dates

**Best date ranges for reliable data:**

1. **Last 30 days** (Option 1)
   - Always works
   - Most recent data
   - All stations have this

2. **Current year** (Option 2)
   - Usually works well
   - Year-to-date analysis

3. **Growing season 2024** (Option 3)
   - Works for recent growing season
   - May-September data

**Avoid:**
- Very old years (before 2000)
- Future dates
- Very long periods (>1 year may timeout)

### 🌡️ Step 4: Choose Better Stations

**Stations with most reliable data:**

| Station | ID | Reliability | Notes |
|---------|-----|-------------|-------|
| Helsinki | 100971 | ⭐⭐⭐⭐⭐ | Best - complete data since 1959 |
| Jokioinen | 101104 | ⭐⭐⭐⭐⭐ | Research station - high quality |
| Tampere | 101118 | ⭐⭐⭐⭐ | Good - complete recent data |
| Turku | 100949 | ⭐⭐⭐⭐ | Good - coastal station |
| Jyväskylä | 101339 | ⭐⭐⭐ | Good - may have some gaps |
| Lepaa | 101267 | ⭐⭐⭐ | Good - educational station |
| Oulu | 101799 | ⭐⭐⭐ | Good - northern data |
| Rovaniemi | 101917 | ⭐⭐ | May have gaps in old data |

### 🔄 Step 5: Understanding the Fallback

The notebook automatically uses **sample data** when API fails. This is:
- ✅ Realistic Finnish weather patterns
- ✅ Proper seasonal variations
- ✅ Good for testing and demonstrations
- ⚠️ Not real historical data
- ⚠️ Use for learning, not research

Sample data simulates:
- Finnish temperature patterns (cold winters, mild summers)
- Seasonal precipitation
- Snow cover patterns
- Day length variations
- Frost periods

## Advanced Troubleshooting

### Check FMI API Manually

Test the API directly in your browser:

```
https://opendata.fmi.fi/wfs?service=WFS&version=2.0.0&request=getFeature&storedquery_id=fmi::observations::weather::daily::simple&fmisid=101104&starttime=2024-01-01T00:00:00Z&endtime=2024-01-31T23:59:59Z
```

Replace:
- `fmisid=101104` with your station ID
- Dates with your desired range

You should see XML data. If you get an error, the API has an issue.

### Check Code Changes

The improved `fetch_fmi_weather_data()` function now:
1. ✅ Tries multiple stored query formats
2. ✅ Provides detailed error messages
3. ✅ Shows exactly what went wrong
4. ✅ Estimates missing data when possible
5. ✅ Gives actionable suggestions

### Enable Debug Mode

To see even more detail, modify the function temporarily:

```python
# In Step 3, after the function definition, add:
import logging
logging.basicConfig(level=logging.DEBUG)
```

This will show full request/response details.

## What the Improved Code Does

The enhanced `fetch_fmi_weather_data()` function now includes:

### 1. Multiple API Attempts
Tries 3 different stored query formats:
- `fmi::observations::weather::daily::simple`
- `fmi::observations::weather::daily::timevaluepair`
- `fmi::observations::weather::multipointcoverage`

### 2. Better Error Messages
Instead of generic "API failed", you now see:
- HTTP status codes
- API error messages
- Data availability info
- Specific suggestions

### 3. Smart Fallbacks
- Estimates min/max temps if only average available
- Fills in missing sunshine hours
- Handles different data formats

### 4. Progress Reporting
Shows exactly what's happening:
- Which query is being tried
- Response status
- Data extraction progress
- Final results

## Still Having Issues?

### Contact FMI Support
- Email: avoin-data@fmi.fi
- Web: https://www.ilmatieteenlaitos.fi/avoin-data-sahkopostiosoite

### Use Alternative Data Sources
If FMI API continues to fail:
1. Download data manually from FMI website
2. Use CSV import instead
3. Use the sample data for demonstrations
4. Try again during off-peak hours

## Summary Checklist

When you see "No data received":

- [ ] Run API Diagnostics cell
- [ ] Check diagnostic results for specific errors
- [ ] Try selecting "Last 30 days" date range
- [ ] Try Helsinki or Jokioinen station
- [ ] Check your internet connection
- [ ] If all else fails, use Sample Data option
- [ ] Report persistent issues to FMI support

## Example: Complete Working Setup

For guaranteed success:

**Step 2 Configuration:**
```
Station: [2] Jokioinen
Time Period: [1] Last 30 days
Thermal Sum: [1] GDD Base 5°C
Historical Comparison: [1] Yes
```

This combination:
- ✅ Reliable station with complete data
- ✅ Recent data (always available)
- ✅ Simple query (fast)
- ✅ Should work 99% of the time

## Questions?

The enhanced error messages will now tell you exactly what's wrong and suggest fixes. Pay attention to the diagnostic output!

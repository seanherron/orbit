===========
Orbit
===========

Orbit provides an easy way to get a number of values, such as current latitude and longitude, from objects in space. Currently, any object with a corresponding Two Line Element (TLE) can be tracked. A list of supported objects is available from Celestrack at <http://www.celestrak.com/NORAD/elements/master.asp>. Usage looks like:

    from orbit import satellite
    
    # 25544 is the idenfier for the International Space Station
    # See http://www.celestrak.com/NORAD/elements/master.asp for an index
    # of identifiers.
    
    iss = satellite(25544)
    
    # Get the current lat/long of the satellite
    iss_current_latitude = iss.lat()
    iss_current_longitude = iss.long()
    
    # Get the proper name of the satellite
    iss_name = iss.name()
    
    # Get the elsat classificiation of the satellite
    iss_elsat_classification = iss.elsat_classification()
    
    # Get the year the satellite launched
    iss_launch_year = iss.launch_year()
    
    # Get the current TLE for the satellite
    iss_tle = iss.tle()
    
    # Get the current elevation of the satellite
    iss_elevation = iss.elevation()
    
    # True if the satellite is currently in the earth's shadow
    iss_eclipsed = iss.eclipsed()
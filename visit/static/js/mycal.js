$('.mycal').easycal({
minTime : '09:00:00',
maxTime : '19:00:00',
slotDuration : 30,
startDate : '31-10-2015',
events : getEvents()
});

$('.mycal').easycal({

columnDateFormat : 'dddd, DD MMM',
timeFormat : 'HH:mm',
minTime : '08:00:00',
maxTime : '19:00:00',
slotDuration : 15, //in mins
dayClick : null,
eventClick : null,
events : [],

widgetHeaderClass : 'ec-day-header',
widgetSlotClass : 'ec-slot',
widgetTimeClass : 'ec-time'

});
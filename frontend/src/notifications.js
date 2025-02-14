//Push notification handling
import { getMessaging, getToken, onMessage } from 'firebase/messaging';

const messaging = getMessaging();

getToken(messaging, { vapidKey: '<YOUR-VAPID-KEY>' })
  .then((currentToken) => {
    if (currentToken) {
      console.log('FCM Token:', currentToken);
    } else {
      console.log('No registration token available');
    }
  })
  .catch((err) => {
    console.error('An error occurred while retrieving token: ', err);
  });

onMessage(messaging, (payload) => {
  console.log('Message received. ', payload);
});

// Add your Firebase configuration here
const firebaseConfig = {
  apiKey: "AIzaSyAQHhtyEAduCAcg6RO2K9J0pegSHs0ldtU",
  authDomain: "ful-class-skeduling-system.firebaseapp.com",
  projectId: "ful-class-skeduling-system",
  storageBucket: "ful-class-skeduling-system.firebasestorage.app",
  messagingSenderId: "421759719229",
  appId: "1:421759719229:web:c1c94c43c8e2bab75a1754"
};

// Initialize Firebase
if (!firebase.apps.length) {
  firebase.initializeApp(firebaseConfig);
}
const auth = firebase.auth();

function signUp(email, password) {
  return auth.createUserWithEmailAndPassword(email, password);
}

function signIn(email, password) {
  return auth.signInWithEmailAndPassword(email, password);
}

function signOut() {
  return auth.signOut();
}

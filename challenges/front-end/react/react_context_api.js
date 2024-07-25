import React, { useState, createContext, useContext } from "react";
import { createRoot } from "react-dom/client";

const languages = ["JavaScript", "Python", "Java", "C++", "C#"];
const LanguageContext = createContext();

function App() {
  const [lang_id, setLangId] = useState(0);

  const toggleLanguage = () => {
    setLangId((lang_id + 1) % languages.length);
  };

  return (
    <LanguageContext.Provider value={{ lang_id, toggleLanguage }}>
      <MainSection />
    </LanguageContext.Provider>
  );
}

function MainSection() {
  const { lang_id, toggleLanguage } = useContext(LanguageContext);

  return (
    <div>
      <p id="favoriteLanguage">
        favorite programming language: {languages[lang_id]}
      </p>
      <button id="changeFavorite" onClick={toggleLanguage}>
        toggle language
      </button>
    </div>
  );
}

const container = document.getElementById("root");
const root = createRoot(container);
root.render(<App />);

import { useState } from "react";
import "../../assets/FiltroConSwitch.css";
export default function FiltroConSwitch({ options, onChange }) {

  if (!options) {
    options = [
      { value: "option1", label: "Option 1" },
      { value: "option2", label: "Option 2" },
      { value: "option3", label: "Option 3" },
      { value: "option4", label: "Option 4" },
    ];
  }

  const [selectedOption, setSelectedOption] = useState(options[0].value);

  const handleOptionChange = (value) => {
    setSelectedOption(value);
    onChange(value);
  };

  return (
    <div className="filtro-con-switch">
        {options.map((option, index) => (
          <div key={index}>
            <input
              type="radio"
              name="select"
              id={`option-${index}`}
              value={option.value}
              checked={selectedOption === option.value}
              onChange={() => handleOptionChange(option.value)}
            />
            <label htmlFor={`option-${index}`} className={`option option-${index}`}>
              <div className="dot"></div>
              <span>{option.label}</span>
            </label>
          </div>
        ))}
      </div>
  );
}

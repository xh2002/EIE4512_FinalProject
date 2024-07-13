import Output from "./components/Output";
import WritingPad from "./components/WritingPad";
import styles from "./index.module.scss";

const App = () => {
  return (
    <div className={styles.container}>
      <WritingPad />
      <Output />
    </div>
  );
};

export default App;

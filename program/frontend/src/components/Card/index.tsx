import classnames from "classnames";
import { ReactNode } from "react";
import styles from "./index.module.scss";

interface CardProps {
  children?: ReactNode;
  className?: string;
}

const Card = ({ className, children }: CardProps) => {
  return <div className={classnames(styles.card, className)}>{children}</div>;
};

export default Card;

import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import App from "./App.jsx";

describe("Research Agent workspace", () => {
  it("renders the research workspace and project form", () => {
    render(<App />);
    expect(screen.getByText(/Automated literature review/i)).toBeTruthy();
    expect(screen.getByLabelText(/Research topic/i)).toBeTruthy();
  });
});

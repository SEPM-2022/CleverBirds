// jest.config.js
module.exports = {
  preset: 'jest-preset-angular',
  setupFilesAfterEnv: ['<rootDir>/setup-jest.ts'],
  globalSetup: 'jest-preset-angular/global-setup',
  coverageThreshold: {
    global: {
      functions: 80,
      lines: 80,
      statements: 80,
      branches: 80
    },
  },
};

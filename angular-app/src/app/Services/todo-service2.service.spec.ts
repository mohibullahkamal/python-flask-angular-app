import { TestBed } from '@angular/core/testing';

import { TodoService2Service } from './todo-service2.service';

describe('TodoService2Service', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: TodoService2Service = TestBed.get(TodoService2Service);
    expect(service).toBeTruthy();
  });
});

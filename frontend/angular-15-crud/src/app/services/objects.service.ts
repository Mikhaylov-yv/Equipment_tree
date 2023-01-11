import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Objects } from '../models/objects.model';

const baseUrl = 'http://localhost:8021/api/objects';

@Injectable({
  providedIn: 'root'
})
export class ObjectsService {

  constructor(private http: HttpClient) { }

  getAll(): Observable<Objects[]> {
    return this.http.get<Objects[]>(baseUrl);
  }
}

<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Run extends Model
{
    protected $fillable = ['file_name', 'grade'];

    protected $with = ['student'];

    public function getFilePathAttribute()
    {
        return 'app/problems/' . $this->problem->id . '/runs/' . $this->id . '/' . $this->file_name;
    }

    public function student()
    {
        return $this->belongsTo(User::class, 'student_id');
    }

    public function problem()
    {
        return $this->belongsTo(Problem::class);
    }
}
